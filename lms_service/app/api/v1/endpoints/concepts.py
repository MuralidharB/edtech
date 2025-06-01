@router.post("/", response_model=ConceptOut)
def create_concept(payload: ConceptCreate, db: Session = Depends(get_db)):
    return crud.create_concept(db, payload)

@router.post("/{id}/add_prerequisite")
def add_edge(id: UUID4, target_id: UUID4, relationship: str, db: Session = Depends(get_db)):
    return crud.add_concept_edge(db, source_id=id, target_id=target_id, relationship=relationship)

@router.post("/versions/save")
def save_version(payload: Dict[str, Any], current_user: User = Depends(get_user), db: Session = Depends(get_db)):
    latest = db.query(ConceptGraphVersion).order_by(ConceptGraphVersion.version_number.desc()).first()
    version = (latest.version_number + 1) if latest else 1

    db.add(ConceptGraphVersion(
        saved_by=current_user.id,
        version_number=version,
        graph_json=payload
    ))
    db.commit()
    return {"status": "saved", "version": version}

@router.post("/course/{course_id}/save_graph")
def save_graph_for_course(course_id: UUID4, payload: Dict[str, Any], db: Session = Depends(get_db)):
    db.query(Concept).filter(Concept.course_id == course_id).delete()
    db.query(ConceptEdge).filter(ConceptEdge.source_id.in_(
        db.query(Concept.id).filter(Concept.course_id == course_id)
    )).delete()

    for node in payload["nodes"]:
        db.add(Concept(
            id=node["id"],
            name=node["label"],
            description=node.get("description", ""),
            course_id=course_id
        ))

    for link in payload["links"]:
        db.add(ConceptEdge(
            source_id=link["source"],
            target_id=link["target"],
            relationship=link.get("type", "requires")
        ))

    db.commit()
    return {"status": "saved"}


@router.get("/course/{course_id}/graph")
def get_course_graph(course_id: UUID4, db: Session = Depends(get_db)):
    concept_ids = db.query(CourseConceptView.concept_id).filter_by(course_id=course_id)
    concepts = db.query(Concept).filter(Concept.id.in_(concept_ids)).all()

    edges = db.query(ConceptEdge).filter(
        ConceptEdge.source_id.in_(concept_ids) |
        ConceptEdge.target_id.in_(concept_ids)
    ).all()

    return {
        "nodes": [{"id": c.id, "label": c.name, "description": c.description} for c in concepts],
        "links": [{"source": e.source_id, "target": e.target_id, "type": e.relationship} for e in edges]
    }


@router.post("/concepts")
def create_concept(payload: Dict[str, str], course_id: UUID4, db: Session = Depends(get_db)):
    c = Concept(name=payload["name"], description=payload.get("description", ""))
    db.add(c)
    db.flush()
    db.add(CourseConceptView(course_id=course_id, concept_id=c.id))
    db.commit()
    return {"id": c.id}


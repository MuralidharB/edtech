@router.post("/", response_model=ConceptOut)
def create_concept(payload: ConceptCreate, db: Session = Depends(get_db)):
    return crud.create_concept(db, payload)

@router.post("/{id}/add_prerequisite")
def add_edge(id: UUID4, target_id: UUID4, relationship: str, db: Session = Depends(get_db)):
    return crud.add_concept_edge(db, source_id=id, target_id=target_id, relationship=relationship)


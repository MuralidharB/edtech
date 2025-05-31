@router.post("/save_graph")
def save_graph(payload: Dict[str, Any], db: Session = Depends(get_db)):
    # Replace existing graph
    db.query(Concept).delete()
    db.query(ConceptEdge).delete()

    for node in payload["nodes"]:
        db.add(Concept(id=node["id"], name=node["label"], description=node.get("description", "")))

    for link in payload["links"]:
        db.add(ConceptEdge(source_id=link["source"], target_id=link["target"], relationship=link["type"]))

    db.commit()
    return {"status": "success"}


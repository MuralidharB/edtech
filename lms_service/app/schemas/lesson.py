class ContentBlockOut(BaseModel):
    type: str
    content: Dict[str, Any]

class LessonOut(BaseModel):
    id: UUID4
    title: str
    sequence_number: int
    content_blocks: List[ContentBlockOut] = []


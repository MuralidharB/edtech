@router.post("/", response_model=LessonOut)
def create_lesson(payload: LessonCreate, db: Session = Depends(get_db)):
    return lesson_crud.create(db, payload)

@router.get("/{lesson_id}", response_model=LessonOut)
def get_lesson(lesson_id: UUID4, db: Session = Depends(get_db)):
    return lesson_crud.get(db, lesson_id)

@router.get("/course/{course_id}/lessons", response_model=List[LessonOut])
def get_lessons_for_course(course_id: UUID4, db: Session = Depends(get_db)):
    return lesson_crud.get_all_by_course(db, course_id)

@router.get("/{lesson_id}", response_model=LessonOut)
def get_lesson_detail(lesson_id: UUID4, db: Session = Depends(get_db)):
    lesson = lesson_crud.get(db, lesson_id)
    content = contentblock_crud.get_by_lesson(db, lesson_id)
    return {
        **lesson.dict(),
        "content_blocks": content
    }

@router.get("/{lesson_id}/next", response_model=LessonOut)
def get_next_lesson(lesson_id: UUID4, db: Session = Depends(get_db)):
    return lesson_crud.get_next(db, lesson_id)

@router.get("/{lesson_id}/recommendation", response_model=LessonOut)
def recommend_next_lesson(lesson_id: UUID4, student_id: UUID4, db: Session = Depends(get_db)):
    current = lesson_crud.get(db, lesson_id)
    quiz_result = submission_crud.get_latest_quiz_result(db, student_id, lesson_id)
    all_lessons = lesson_crud.get_all_by_course(db, current.course_id)

    recommended = adaptive_engine.recommend_next_lesson(current.id, quiz_result, all_lessons)
    return recommended



from typing import List, Dict
from app.db.models.lesson import Lesson

def recommend_next_lesson(current_lesson_id: str, quiz_result: Dict, available_lessons: List[Lesson]):
    # Simple heuristic for prototype
    weak_topics = [q['question_id'] for q in quiz_result['responses'] if not q['correct']]
    
    for lesson in available_lessons:
        if any(tag in lesson.metadata.get('tags', []) for tag in weak_topics):
            return lesson  # prioritized remediation
    return sorted(available_lessons, key=lambda l: l.sequence_number)[0]

def get_missing_prerequisites(concepts: List[str], graph: nx.DiGraph):
    missing = set()
    for c in concepts:
        if c in graph:
            for pre in graph.predecessors(c):
                if not student_has_mastered(pre):  # via submissions or tracking
                    missing.add(pre)
    return list(missing)


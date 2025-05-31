def grade_quiz(questions: list, answers: list) -> dict:
    answer_map = {a.question_id: a.answer for a in answers}
    score = 0
    responses = []

    for q in questions:
        qid = q["id"]
        student_answer = answer_map.get(qid, "")
        correct = False
        feedback = None

        if q["type"] == "multiple_choice":
            correct = student_answer == q["correct"]

        elif q["type"] == "short_answer":
            keywords = q.get("correct_keywords", [])
            correct = all(k.lower() in student_answer.lower() for k in keywords)
            feedback = "Check if you've covered key terms."

        if correct:
            score += 1

        responses.append({
            "question_id": qid,
            "answer": student_answer,
            "correct": correct,
            "feedback": feedback
        })

    return {
        "score": score,
        "total": len(questions),
        "responses": responses
    }

def grade_quiz_with_weights(questions: list, answers: list) -> dict:
    answer_map = {a.question_id: a.answer for a in answers}
    score = 0
    max_total = 0
    responses = []

    for q in questions:
        qid = q["id"]
        weight = q.get("weight", 1)
        max_total += weight
        student_answer = answer_map.get(qid, "")
        correct = False

        if q["type"] == "multiple_choice":
            correct = student_answer == q["correct"]
        elif q["type"] == "short_answer":
            correct = all(k.lower() in student_answer.lower() for k in q.get("correct_keywords", []))

        earned = weight if correct else 0
        score += earned

        responses.append({
            "question_id": qid,
            "answer": student_answer,
            "score": earned,
            "max_score": weight,
            "correct": correct
        })

    return {
        "score": score,
        "total": max_total,
        "responses": responses
    }


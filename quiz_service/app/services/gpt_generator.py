# app/services/gpt_generator.py
import openai
from typing import List
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_quiz_questions(context: str, count: int = 5, difficulty: str = "medium", qtype: str = "mcq") -> List[dict]:
    prompt = f"""
    You are an educational quiz generator for 6th grade.
    Generate {count} {difficulty} {qtype.upper()} questions based on this lesson:
    """
    prompt += f"\n\n{context}\n\n"
    prompt += "Output in JSON array with: question_text, type, options, correct_answer, explanation."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )
    output = response.choices[0].message.content
    return eval(output)  # TODO: Replace with safe parser


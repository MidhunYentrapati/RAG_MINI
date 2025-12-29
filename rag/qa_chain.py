import google.generativeai as genai
from typing import List, Dict
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)


def build_context(chunks: List[Dict]) -> str:
    """
    Build a single context string from retrieved chunks.
    """
    context_blocks = []

    for chunk in chunks:
        block = f"(Page {chunk['page']}): {chunk['text']}"
        context_blocks.append(block)

    return "\n\n".join(context_blocks)


def answer_question(
    question: str,
    retrieved_chunks: List[Dict]
) -> str:
    """
    Generate an answer grounded strictly in retrieved context.
    """
    context = build_context(retrieved_chunks)

    prompt = f"""
You are a document-based assistant.

Answer the question ONLY using the context below.
If the answer is not present in the context, say:
"Answer not found in the provided document."

Context:
{context}

Question:
{question}

Answer:
"""

    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return response.text.strip()

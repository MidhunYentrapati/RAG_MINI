'''
import google.generativeai as genai
from typing import List
from config import GEMINI_API_KEY, EMBEDDING_MODEL

genai.configure(api_key=GEMINI_API_KEY)


def embed_texts(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for a list of texts using Gemini.
    """
    embeddings = []

    for text in texts:
        response = genai.embed_content(
            model=EMBEDDING_MODEL,
            content=text,
            task_type="retrieval_document"
        )
        embeddings.append(response["embedding"])

    return embeddings


def embed_query(query: str) -> List[float]:
    """
    Generate embedding for a user query.
    """
    response = genai.embed_content(
        model=EMBEDDING_MODEL,
        content=query,
        task_type="retrieval_query"
    )
    return response["embedding"]
'''
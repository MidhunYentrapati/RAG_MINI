from sentence_transformers import SentenceTransformer
from typing import List

# Small, fast, high-quality model
_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts: List[str]) -> List[List[float]]:
    """
    Generate embeddings for documents (local, free).
    """
    return _model.encode(texts, convert_to_numpy=True).tolist()


def embed_query(query: str) -> List[float]:
    """
    Generate embedding for user query.
    """
    return _model.encode(query, convert_to_numpy=True).tolist()

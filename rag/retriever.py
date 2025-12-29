import numpy as np
from typing import List, Dict
from rag.embeddings import embed_query
from rag.vector_store import load_vector_store


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 5
) -> List[Dict]:
    """
    Retrieve top-k relevant chunks for a user query.
    """
    # Load FAISS index and metadata
    index, metadata = load_vector_store()

    # Embed query
    query_embedding = embed_query(query)
    query_vector = np.array([query_embedding]).astype("float32")

    # Perform similarity search
    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(metadata):
            results.append(metadata[idx])

    return results

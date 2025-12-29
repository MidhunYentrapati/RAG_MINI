import os
import pickle
import faiss
import numpy as np
from typing import List, Dict
from config import FAISS_INDEX_PATH, METADATA_PATH


def create_faiss_index(embeddings: List[List[float]]):
    """
    Create a FAISS index from embeddings.
    """
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index


def save_vector_store(index, metadata: List[Dict]):
    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)

    faiss.write_index(index, FAISS_INDEX_PATH)

    with open(METADATA_PATH, "wb") as f:
        pickle.dump(metadata, f)


def load_vector_store():
    index = faiss.read_index(FAISS_INDEX_PATH)

    with open(METADATA_PATH, "rb") as f:
        metadata = pickle.load(f)

    return index, metadata

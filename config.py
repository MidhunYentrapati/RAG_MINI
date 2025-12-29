import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

EMBEDDING_MODEL = "models/gemini-embedding-001"

FAISS_INDEX_PATH = "vector_store/faiss.index"
METADATA_PATH = "vector_store/metadata.pkl"
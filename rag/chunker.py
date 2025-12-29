# Phase 2 - Chunking

from typing import List, Dict

def chunk_text(
        pages: List[Dict],
        chunk_size: int = 500,
        chunk_overlap: int = 100
) -> List[Dict]:
    
    chunks = []
    chunk_id = 0

    for page in pages:
        text = page["text"]
        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "chunk_id": chunk_id,
                "page": page["page"],
                "text": chunk_text
            })

            chunk_id += 1
            start = end - chunk_overlap

    return chunks
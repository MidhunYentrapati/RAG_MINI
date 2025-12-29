# Phase 1 - PDF Ingestion

import fitz
from typing import List, Dict

def load_pdf(file_path : str) -> List[Dict]:
    doc = fitz.open(file_path)
    pages = []

    for pg_no in range(len(doc)):
        page = doc[pg_no]
        text = page.get_text("text")

        # Cleaning
        text = text.replace("\n", " ").replace("\t", " ")
        text = " ".join(text.split())

        if text.strip():
            pages.append({
                "page": pg_no +1,
                "text": text
            })

    doc.close()
    return pages
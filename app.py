import streamlit as st
import os
import tempfile

from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embeddings import embed_texts
from rag.vector_store import create_faiss_index, save_vector_store
from rag.retriever import retrieve_relevant_chunks
from rag.qa_chain import answer_question


st.set_page_config(page_title="Chat with PDF (Gemini RAG)", layout="wide")

st.title("📄 Chat with PDF using Gemini (RAG)")
st.caption("Ask questions grounded strictly in your document")

# Session state flags
if "indexed" not in st.session_state:
    st.session_state.indexed = False


# -------------------------------
# PDF Upload & Indexing
# -------------------------------
st.sidebar.header("Upload PDF")

uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF document",
    type=["pdf"]
)

if uploaded_file and not st.session_state.indexed:
    with st.spinner("Processing PDF and building knowledge base..."):
        # Save uploaded PDF temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            pdf_path = tmp_file.name

        # Pipeline: Load → Chunk → Embed → Store
        pages = load_pdf(pdf_path)
        chunks = chunk_text(pages)

        texts = [chunk["text"] for chunk in chunks]
        embeddings = embed_texts(texts)

        index = create_faiss_index(embeddings)
        save_vector_store(index, chunks)

        st.session_state.indexed = True

        os.remove(pdf_path)

    st.sidebar.success("PDF indexed successfully ✅")


# -------------------------------
# Question Answering
# -------------------------------
st.subheader("Ask a question")

query = st.text_input(
    "Enter your question about the document",
    disabled=not st.session_state.indexed
)

if query:
    with st.spinner("Searching document and generating answer..."):
        retrieved_chunks = retrieve_relevant_chunks(query, top_k=5)
        answer = answer_question(query, retrieved_chunks)

    st.markdown("### 🧠 Answer")
    st.write(answer)

    st.markdown("### 📌 Source Pages")
    pages = sorted(set(chunk["page"] for chunk in retrieved_chunks))
    st.write(", ".join(f"Page {p}" for p in pages))

Chat with PDF using RAG & Gemini LLM

A Retrieval-Augmented Generation (RAG) based application that enables users to chat with PDF documents using semantic search and LLM-based, context-grounded answers.

This project is intentionally designed to be small, clean, and impactful, demonstrating real-world GenAI system design rather than a toy demo.

Features:

Upload and process PDF documents
Intelligent text chunking with overlap
Semantic search using vector embeddings + FAISS
Context-grounded question answering using Gemini LLM
Hallucination control (answers strictly from document content)
Source page attribution for transparency
Interactive Streamlit UI


System Architecture:

PDF
 ↓
PyMuPDF (Text Extraction)
 ↓
Chunking (Overlap + Metadata)
 ↓
Local Embeddings (SentenceTransformers)
 ↓
FAISS Vector Store
 ↓
Semantic Retrieval (Top-K)
 ↓
Gemini LLM (Context-Grounded QA)
 ↓
Streamlit UI


Tech Stack:

UI -> Streamlit
PDF Parsing -> PyMuPDF
Chunking -> Custom Python logic
Embeddings -> SentenceTransformers (all-MiniLM-L6-v2)
Vector Store -> FAISS
LLM -> Google Gemini Pro
Language -> Python
 

Project Structure

RAG_MINI/
│
├── app.py                      # Streamlit app
├── config.py                   # Configurations
├── requirements.txt
│
├── rag/
│   ├── loader.py               # PDF extraction
│   ├── chunker.py              # Text chunking
│   ├── embeddings.py           # Embedding generation
│   ├── vector_store.py         # FAISS index handling
│   ├── retriever.py            # Semantic retrieval
│   └── qa_chain.py             # Gemini-based QA
│
├── vector_store/
│   ├── faiss.index
│   └── metadata.pkl


How RAG Is Implemented

1. Document Ingestion
- Extracts text page-wise using PyMuPDF
- Skips empty or noisy pages
2. Chunking
- Fixed-size chunks with overlap
- Preserves page metadata for traceability
3. Embeddings
- Uses local SentenceTransformer embeddings
- Chosen for cost-efficiency and reliability
4. Vector Storage
- FAISS stores dense vectors
- Metadata stored separately
5. Retrieval
- Query is embedded
- Top-K relevant chunks retrieved via similarity search
6. Answer Generation
- Gemini LLM answers strictly using retrieved context
- Returns fallback if answer is not found in document

Hallucination Control
- The LLM is explicitly instructed to:
- Use only the retrieved document context
- Avoid guessing or external knowledge


▶️ Running the Application
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Set Gemini API Key
GEMINI_API_KEY="your_api_key_here"


(On Windows PowerShell)

setx GEMINI_API_KEY "your_api_key_here"

3️⃣ Start the App
streamlit run app.py

🧪 Example Use Cases

Ask questions from academic PDFs

Query long reports or documentation

Resume-ready demo for RAG / GenAI interviews

Internal knowledge assistant prototype

⚙️ Design Decisions & Tradeoffs

Local embeddings were used instead of Gemini embeddings due to:

Free-tier quota limitations

Better cost control

Faster indexing

Architecture is embedding-provider agnostic

Separation of concerns follows production best practices

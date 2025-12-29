Chat with PDF — RAG-based Q&A using Gemini

A small but production-style Retrieval-Augmented Generation (RAG) system that enables users to ask questions from PDF documents and receive context-grounded answers.

This project focuses on core RAG engineering — chunking, embeddings, retrieval, and hallucination control — without relying on heavy abstractions or black-box frameworks.

Why this project exists

Most “Chat with PDF” demos:

Hide logic behind frameworks

Ignore real API and cost constraints

Hallucinate answers confidently

This project was built to:

Implement RAG end-to-end from scratch

Handle real-world constraints such as API quotas and cost

Keep the system modular, explainable, and debuggable

High-level flow
PDF
 → Text Extraction (PyMuPDF)
 → Chunking (overlap + metadata)
 → Embeddings (local)
 → FAISS Vector Store
 → Top-K Semantic Retrieval
 → Gemini LLM (context-grounded answer)
 → Streamlit UI

Tech stack
Layer	Technology
UI	Streamlit
PDF Parsing	PyMuPDF
Chunking	Custom Python logic
Embeddings	SentenceTransformers (all-MiniLM-L6-v2)
Vector Store	FAISS
LLM	Google Gemini Pro
Language	Python
Key design decisions
1. No LangChain or heavy abstractions

The entire pipeline is implemented using plain Python modules.

This provides full control over:

Chunk boundaries

Retrieval quality

Hallucination behavior

and makes the system easier to debug and reason about.

2. Local embeddings instead of hosted embeddings

Gemini embeddings were initially evaluated.

Due to free-tier quota limitations, the system was intentionally switched to local sentence-transformer embeddings.

Benefits of this approach:

Zero cost

No rate limits

Faster indexing

Embedding-provider agnostic architecture

3. Strict hallucination control

The LLM is explicitly instructed to:

Answer only from retrieved document context

Avoid using external or prior knowledge

Return a clear fallback when information is missing

This ensures responses are trustworthy, not just fluent.

4. Metadata-first design

Each chunk retains:

Page number

Chunk ID

Original text

This enables:

Source attribution

Easier debugging

UI transparency

Project structure
RAG_MINI/
│
├── app.py                 # Streamlit entry point
├── config.py              # Environment-based configuration
├── requirements.txt
│
├── rag/
│   ├── loader.py          # PDF text extraction
│   ├── chunker.py         # Overlap-aware chunking
│   ├── embeddings.py     # Embedding generation
│   ├── vector_store.py   # FAISS index handling
│   ├── retriever.py      # Semantic retrieval
│   └── qa_chain.py       # Gemini-based QA
│
├── vector_store/          # Local FAISS index (gitignored)
└── .gitignore

How RAG works in this project

PDF is parsed page-wise using PyMuPDF

Text is split into overlapping chunks with metadata

Chunks are embedded and stored in FAISS

User query is embedded and matched via similarity search

Top-K chunks are passed as explicit context to Gemini

Gemini generates a grounded answer or a safe fallback

Running locally
1. Install dependencies
pip install -r requirements.txt

2. Set API key (via environment variable)

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here


The .env file is ignored by Git and never committed.

3. Run the application
streamlit run app.py

What this project demonstrates

End-to-end understanding of RAG systems

Practical handling of LLM limitations and quotas

Clean separation of concerns

Production-style vector search design

Hallucination-aware prompting

# Cyber Op RAG Chatbot

This is a secure, hosted Retrieval-Augmented Generation (RAG) chatbot for Cyber Op. It leverages GPT-4 and PDF documents to answer cybersecurity-related questions.

## 🔧 Setup

1. Clone the repo
2. Add your OpenAI API key to `.env`
3. Run `docker-compose up --build`

## 📁 Upload Files
Upload PDF documents via `/upload` endpoint for embedding.

## 🧠 Query
Use `/query` endpoint with a question. The LLM answers using relevant chunks.

## 🔐 Security Tips

- Use HTTPS in production
- Restrict IPs or add JWT auth on all endpoints
- Store uploaded PDFs securely (consider S3 private bucket)
- Sanitize file uploads (filename filters, antivirus scanner)
- Monitor and rate-limit queries to prevent API overuse

## 🧪 Testing
Try uploading real redacted logs and SOPs and ask structured questions.

## 🧰 Stack
- FastAPI
- ChromaDB
- OpenAI GPT-4 API
- React (Tailwind + ShadCN ready)
- Dockerized
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz  # PyMuPDF
import openai
import chromadb

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = "<OPENAI_API_KEY>"
client = chromadb.Client()
collection = client.get_or_create_collection("cyberop")

class Query(BaseModel):
    question: str

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    doc = fitz.open(stream=await file.read(), filetype="pdf")
    chunks = []
    for page in doc:
        text = page.get_text()
        chunks.append(text)
        collection.add(documents=[text], ids=[f"{file.filename}-{page.number}"])
    return {"status": "uploaded", "chunks": len(chunks)}

@app.post("/query")
async def query_docs(q: Query):
    results = collection.query(query_texts=[q.question], n_results=3)
    context = "\n".join([r for r in results["documents"][0]])
    prompt = f"You are a cybersecurity assistant for Cyber Op. Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {q.question}\nAnswer:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"answer": response["choices"][0]["message"]["content"]}
import fitz
from openai import OpenAIEmbeddings

def extract_chunks_from_pdf(file_path):
    doc = fitz.open(file_path)
    chunks = []
    for page in doc:
        text = page.get_text()
        chunks.append(text.strip())
    return chunks
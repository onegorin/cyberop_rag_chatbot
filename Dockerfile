FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY docs ./docs

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
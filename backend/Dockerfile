FROM python:3.9-slim

WORKDIR /MEU-PROJETO

COPY . .

RUN pip install fastapi uvicorn httpx

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

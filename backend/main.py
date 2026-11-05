"""Punto de entrada de Aruba API Explorer."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Aruba API Explorer", description="Backend para explorar Aruba Central VisualRF.", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"], allow_credentials=False, allow_methods=["GET", "POST"], allow_headers=["Content-Type", "Authorization"])

@app.get("/")
async def root():
    return {"application": "Aruba API Explorer", "version": "0.1.0", "status": "running"}

@app.get("/api/health")
async def health():
    return {"status": "ok", "message": "El backend está funcionando.", "aruba_integration": "pending_configuration"}

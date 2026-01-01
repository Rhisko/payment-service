from fastapi import FastAPI
from app.routes import router
from app.config import DEBUG

app = FastAPI(debug=DEBUG)

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}

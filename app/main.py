from fastapi import FastAPI
from app.routes import router
from app.config import DEBUG
import pandas as pd
import numpy as np

app = FastAPI(debug=DEBUG)

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok"}


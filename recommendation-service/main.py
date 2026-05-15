from fastapi import FastAPI
import joblib
import pandas as pd
import os

app = FastAPI(title="Recommendation Service")

MODEL_PATH = "model/model.pkl"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/recommendations/{user_id}")
def recommend(user_id: int):
    if not os.path.exists(MODEL_PATH):
        return {"error": "Model not found"}

    model = joblib.load(MODEL_PATH)
    recs = model.get(user_id, [])
    return {"user_id": user_id, "recommendations": recs}

@app.post("/train")
def train_model():
    os.system("python train.py")
    return {"message": "Model trained"}
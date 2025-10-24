from fastapi import FastAPI, HTTPException
import joblib
import numpy as np
from pathlib import Path
from .schemas import HeartData

app = FastAPI(
    title="Heart Disease Prediction API",
    version="1.0.0",
    description="Demo API for Docker/Render assignment. Focus on deploy, not SOTA accuracy."
)

MODEL_PATH = Path(__file__).resolve().parents[1] / "model" / "heart_model.joblib"

# Lazy-load model (gives a friendly error if you forgot to train)
_model = None
def get_model():
    global _model
    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model not found at {MODEL_PATH}. Run `python train_model.py` first."
            )
        _model = joblib.load(MODEL_PATH)
    return _model

FEATURES = [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal"
]

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/info")
def info():
    return {
        "model_file": MODEL_PATH.name,
        "features": FEATURES,
        "notes": "Pydantic v2 + FastAPI; simple sklearn pipeline saved with joblib."
    }

@app.post("/predict")
def predict(data: HeartData):
    try:
        model = get_model()
    except FileNotFoundError as e:
        raise HTTPException(status_code=500, detail=str(e))

    X = np.array([[
        data.age, data.sex, data.cp, data.trestbps, data.chol, data.fbs,
        data.restecg, data.thalach, data.exang, data.oldpeak, data.slope,
        data.ca, data.thal
    ]], dtype=float)

    yhat = model.predict(X)[0]
    return {"heart_disease": bool(int(yhat))}

"""
main.py
-------
FastAPI backend that loads the trained model + vectorizer and exposes
a /predict endpoint for the frontend to call.

Run locally with:
    uvicorn main:app --reload

Then open http://127.0.0.1:8000/docs to test it in the browser,
or open frontend/index.html in your browser to use the actual UI.
"""

import os

import joblib
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from utils import full_pipeline

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "vectorizer.pkl")

app = FastAPI(title="Sentiment Analysis API")

# Allow the frontend (served from a different origin/file) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Load model + vectorizer once, at startup (not on every request).
# ---------------------------------------------------------------------------
model = None
vectorizer = None


@app.on_event("startup")
def load_model():
    global model, vectorizer
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise RuntimeError(
            "model.pkl / vectorizer.pkl not found. "
            "Run training/train_model.py first to generate them."
        )
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("Model and vectorizer loaded successfully.")


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------
class PredictRequest(BaseModel):
    text: str


class PredictResponse(BaseModel):
    text: str
    prediction: str
    confidence: float


@app.get("/")
def root():
    return {"message": "Sentiment Analysis API is running. See /docs for usage."}


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": model is not None}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text field cannot be empty.")

    processed = full_pipeline(text)
    if not processed:
        # Nothing left after cleaning (e.g. text was only punctuation/numbers)
        raise HTTPException(
            status_code=400,
            detail="No meaningful text found after preprocessing.",
        )

    features = vectorizer.transform([processed])
    prediction = model.predict(features)[0]

    # Confidence = probability of the predicted class
    probabilities = model.predict_proba(features)[0]
    confidence = float(max(probabilities))

    return PredictResponse(text=text, prediction=prediction, confidence=confidence)

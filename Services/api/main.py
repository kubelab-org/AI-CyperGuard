# services/api/main.py
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI(title="AI-CyberGuard API")

# Define input data model
class DataInput(BaseModel):
    features: list[float]

# Root endpoint
@app.get("/")
def root():
    return {"message": "AI-CyberGuard API is running."}

# Dummy prediction endpoint
@app.post("/predict")
def predict(data: DataInput):
    # Example logic: classify based on sum of features
    total = sum(data.features)
    label = "malicious" if total > 10 else "normal"
    return {"prediction": label, "total": total}

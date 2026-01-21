from fastapi import FastAPI
import joblib

app = FastAPI(title="Sentiment API")

model = joblib.load("mvp_sentimientos.joblib")

@app.post("/predict")
def predict(text: str):
    pred = model.predict([text])[0]
    return {"sentiment": pred}

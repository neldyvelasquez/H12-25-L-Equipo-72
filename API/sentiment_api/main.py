
from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import numpy as np

app = FastAPI(
    title="Sentiment Analysis API",
    description="""
### Hackatón Alura Latam – Equipo Grupo 72

API desarrollada para la Hackatón Alura Latam.

Servicio de análisis de sentimiento binario (positivo / negativo)
entrenado con textos **exclusivamente en inglés**.

⚠️ El texto enviado debe estar en idioma inglés.
""",
    version="1.0.0-hackathon"
)

# ----------------------------------------------------------
# Carga de modelos
# ----------------------------------------------------------
modelo = joblib.load("modelo_sentimiento.pkl")
vectorizer = joblib.load("vectorizer.pkl")
model_signature = joblib.load("model_signature.pkl")

# ----------------------------------------------------------
# Esquema de entrada
# ----------------------------------------------------------
class TextInput(BaseModel):
    text: str = Field(
        ...,
        example="I really loved the service"
    )

# ----------------------------------------------------------
# Endpoint de predicción
# ----------------------------------------------------------
@app.post(
    "/sentiment",
    summary="Clasificación de sentimiento (texto en inglés)"
)
def predict_sentiment(data: TextInput):
    X = vectorizer.transform([data.text])
    proba = modelo.predict_proba(X)[0]
    clase = int(np.argmax(proba))

    sentiment = "Positivo" if clase == 1 else "Negativo"
    confidence = round(float(proba[clase]) * 100, 2)

    return {
        "sentiment": sentiment,
        "confidence": confidence
    }

# ----------------------------------------------------------
# Endpoint información del modelo
# ----------------------------------------------------------
@app.get("/model-info")
def model_info():
    return model_signature

# ----------------------------------------------------------
# Health check
# ----------------------------------------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "language_requirement": "English only"
    }

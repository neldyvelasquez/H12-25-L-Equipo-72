# Sentiment Analysis API – Hackatón Alura Latam

API de clasificación de sentimiento **binario (positivo / negativo)**.

⚠️ El modelo fue entrenado **solo con textos en inglés**.

## Endpoint principal

POST /sentiment

### Body

```json
{
  "text": "I really loved the service"
}
```

### Respuesta esperada

```json
{
  "sentiment": "Positivo",
  "confidence": 51.35
}
```

## Endpoints adicionales

- GET /model-info
- GET /health

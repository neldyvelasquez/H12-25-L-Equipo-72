# H12-25-L-Equipo 72

## Proyecto 1: SentimentAPI — Análisis de Sentimientos de Feedbacks ONE

## 1. Análisis del proyecto

### 1.1 Problema de negocio
Las empresas reciben grandes volúmenes de comentarios (reseñas, encuestas, redes sociales) y no pueden analizarlos manualmente. Esto genera:
- Lentitud en la atención al cliente
- Pérdida de oportunidades de mejora
- Dificultad para medir la satisfacción en el tiempo

### 1.2 Solución propuesta
Una API de análisis de sentimiento que:
- Recibe un texto
- Clasifica el sentimiento (Positivo / Neutro / Negativo o binario)
- Devuelve la predicción con su probabilidad
- Puede integrarse fácilmente con otros sistemas

### 1.3 Valor para el cliente
Incluso con un modelo simple:
- Prioriza comentarios negativos
- Monitorea campañas de marketing
- Detecta tendencias de satisfacción
- Reduce esfuerzo manual

### 1.4 Alcance técnico adecuado al hackathon
- Modelo clásico de NLP: TF-IDF + Regresión Logística o Naive Bayes
- API REST simple
- Integración clara entre Data Science (DS) y Back-End (BE)
- MVP funcional sobre sofisticación excesiva

---

## FASE 1 – Definición y alineación (DS + BE)

### 1.1 Definir alcance funcional
**Responsables:** DS + BE  
**Dependencias:** Ninguna

- Definir:
  - Clasificación binaria o ternaria
  - Idioma (Español / Portugués / ambos)

- Contrato de integración JSON

#### Entrada
```json
{
  "text": "El servicio fue excelente"
}


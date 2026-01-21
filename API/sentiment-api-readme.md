# 🧠 Sentiment Analysis API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

> **Hackatón Alura Latam – Equipo Grupo 72**

API RESTful de alto rendimiento para el análisis de sentimiento binario. Diseñada para clasificar textos y opiniones de clientes de manera automática utilizando Machine Learning.

---

## 📋 Descripción

Este servicio expone un modelo de aprendizaje automático entrenado para detectar polaridad **(Positivo / Negativo)** en textos. Es ideal para automatizar el procesamiento de feedback de clientes, reseñas de productos o monitoreo de redes sociales.

> ⚠️ **Nota Importante:** El modelo actual ha sido entrenado y optimizado para textos exclusivamente en **Inglés**.

### ✨ Características Principales

- **Clasificación Binaria:** Detección precisa de sentimientos positivos y negativos
- **Confidence Score:** Devuelve la probabilidad asociada a cada predicción
- **Arquitectura Ligera:** Construido sobre FastAPI para respuestas en milisegundos
- **Health Checks:** Endpoints dedicados para monitoreo de salud y metadatos del modelo

---

## 🛠️ Tecnologías

El proyecto utiliza un stack moderno de Ciencia de Datos y Backend:

- **Core:** [Python](https://www.python.org/)
- **API Framework:** [FastAPI](https://fastapi.tiangolo.com/) + [Uvicorn](https://www.uvicorn.org/)
- **ML & Data:** [Scikit-learn](https://scikit-learn.org/), [NumPy](https://numpy.org/)
- **Serialización:** Joblib

---

## 🚀 Instalación y Ejecución

Sigue estos pasos para levantar el entorno localmente:

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/sentiment-api.git
cd sentiment-api
```

### 2️⃣ Instalar dependencias

Se recomienda usar un entorno virtual (`venv` o `conda`):

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 3️⃣ Iniciar el servidor

```bash
uvicorn main:app --reload
```

✅ **El servidor estará disponible en:** `http://127.0.0.1:8000`

📚 **Documentación interactiva:** `http://127.0.0.1:8000/docs`

---

## 🔌 Documentación de Endpoints

### 📊 `POST /sentiment` - Predecir Sentimiento

Analiza el texto enviado y retorna la clasificación.

**Request:**

```json
{
  "text": "I really loved the service, it was amazing!"
}
```

**Response:**

```json
{
  "sentiment": "Positivo",
  "confidence": 98.5
}
```

### ℹ️ `GET /model-info` - Información del Modelo

Retorna metadatos técnicos sobre el modelo cargado (versión, firma, métricas).

**Response:**

```json
{
  "model_type": "LogisticRegression",
  "vectorizer": "TfidfVectorizer",
  "language": "English",
  "accuracy": 0.92
}
```

### 💚 `GET /health` - Health Check

Verifica si la API está operativa.

**Response:**

```json
{
  "status": "ok",
  "language_requirement": "English only"
}
```

---

## 🧪 Pruebas Rápidas

Puedes probar la API directamente desde tu terminal usando `curl`:

### ✅ Prueba Positiva

```bash
curl -X POST "http://127.0.0.1:8000/sentiment" \
     -H "Content-Type: application/json" \
     -d '{"text": "This is the best experience I have ever had"}'
```

### ❌ Prueba Negativa

```bash
curl -X POST "http://127.0.0.1:8000/sentiment" \
     -H "Content-Type: application/json" \
     -d '{"text": "The service was terrible and slow"}'
```

### 🐍 Prueba con Python

```python
import requests

url = "http://127.0.0.1:8000/sentiment"
data = {"text": "The product quality exceeded my expectations!"}

response = requests.post(url, json=data)
print(response.json())
```

---

## 📂 Estructura del Proyecto

```
sentiment-api/
├── main.py                    # Punto de entrada FastAPI
├── modelo_sentimiento.pkl     # Modelo ML serializado
├── vectorizer.pkl             # Vectorizador TF-IDF
├── requirements.txt           # Dependencias Python
├── README.md                  # Documentación
└── tests/                     # Tests unitarios (opcional)
```

### 📄 Descripción de Archivos

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Punto de entrada de la aplicación FastAPI y lógica de endpoints |
| `modelo_sentimiento.pkl` | Modelo de Regresión Logística serializado con Joblib |
| `vectorizer.pkl` | Vectorizador TF-IDF ajustado al corpus de entrenamiento |
| `requirements.txt` | Lista de dependencias del proyecto con versiones |

---

## 📦 Dependencias Principales

```txt
fastapi==0.68.0
uvicorn[standard]==0.15.0
scikit-learn==1.0.0
numpy==1.21.0
joblib==1.1.0
pydantic==1.8.2
```

---

## 🎯 Casos de Uso

- **E-commerce:** Análisis automático de reseñas de productos
- **Atención al Cliente:** Clasificación de tickets por urgencia emocional
- **Redes Sociales:** Monitoreo de menciones de marca
- **Encuestas:** Procesamiento masivo de feedback abierto

---

## 🔮 Roadmap

- [ ] Soporte para español y otros idiomas
- [ ] Análisis de sentimiento multiclase (Positivo/Neutral/Negativo)
- [ ] Detección de emociones específicas (alegría, enojo, tristeza)
- [ ] API de batch processing para múltiples textos
- [ ] Dashboard de visualización en tiempo real

---

## 👥 Equipo

**Grupo 72 - Hackatón Alura Latam**

Desarrollado con ❤️ y ☕ por el equipo del Grupo 72

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📧 Contacto

¿Preguntas o sugerencias? Contáctanos a través de:

- 📧 Email: grupo72@aluralatam.com
- 💬 Discord: Servidor Alura Latam
- 🐦 Twitter: [@AluraLatam](https://twitter.com/aluralatam)

---

<div align="center">

**⭐ Si te gustó este proyecto, déjanos una estrella en GitHub ⭐**

</div>
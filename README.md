# 😊 Sentiment Analysis Web Application

An end-to-end AI-powered Sentiment Analysis Web Application built using **Machine Learning**, **Natural Language Processing (NLP)**, **FastAPI**, and **HTML/CSS/JavaScript**.

The application predicts whether a user's text expresses a **Positive**, **Neutral**, or **Negative** sentiment.

---

## 🚀 Features

- Text Cleaning & Preprocessing
- TF-IDF Feature Extraction
- Logistic Regression Classifier
- Confidence Score Prediction
- FastAPI REST API
- Interactive Web Interface
- Swagger API Documentation
- End-to-End Machine Learning Pipeline

---

# 🛠 Tech Stack

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- NLTK
- FastAPI
- HTML
- CSS
- JavaScript
- Git & GitHub

---

# 📁 Project Structure

```text
Sentiment-Analysis-WebApp/
│
├── backend/
│   ├── main.py
│   ├── utils.py
│   ├── model.pkl
│   ├── vectorizer.pkl
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── dataset/
│   └── sentiment_data.csv
│
├── training/
│   └── train_model.ipynb
│
├── README.md
└── .gitignore
```

---

# 📊 Machine Learning Workflow

```
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Text Preprocessing
   │
   ▼
TF-IDF Vectorization
   │
   ▼
Train Logistic Regression Model
   │
   ▼
Model Evaluation
   │
   ▼
Save Model (.pkl)
   │
   ▼
FastAPI Backend
   │
   ▼
Frontend
```

---

# 📂 Dataset

This project uses the **Sentiment Analysis Dataset** from Kaggle.

**Dataset Link**

https://www.kaggle.com/datasets/abdelmalekeladjelet/sentiment-analysis-dataset

The dataset contains user comments labeled into three sentiment classes:

- Positive
- Neutral
- Negative

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Sentiment-Analysis-WebApp.git
```

Go to project folder

```bash
cd Sentiment-Analysis-WebApp
```

Install dependencies

```bash
pip install -r backend/requirements.txt
```

---

# 🧠 Train the Model

Open

```
training/train_model.ipynb
```

Run all cells.

The notebook performs:

- Dataset Exploration
- Data Cleaning
- Text Preprocessing
- TF-IDF Vectorization
- Model Training
- Model Evaluation
- Saving Trained Model

Generated files:

```
backend/model.pkl
backend/vectorizer.pkl
```

---

# ▶️ Run FastAPI Backend

```bash
cd backend
uvicorn main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 🌐 Run Frontend

Open

```
frontend/index.html
```

or run a local server

```bash
cd frontend
python -m http.server 5500
```

Then visit

```
http://localhost:5500
```

---

# 📌 API Endpoint

## POST /predict

Example Request

```json
{
    "text":"I love this internship."
}
```

Example Response

```json
{
    "text":"I love this internship.",
    "prediction":"Positive",
    "confidence":0.996
}
```

---

# 🧪 Testing

Test the application using:

- Positive sentences
- Negative sentences
- Neutral sentences
- Empty input
- Long paragraphs

---

# 📈 Model

Algorithm Used

- Logistic Regression

Feature Extraction

- TF-IDF Vectorizer

Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

# 🔮 Future Improvements

- Deep Learning Models (LSTM/BERT)
- Dark Mode
- Multi-language Sentiment Analysis
- Speech-to-Text Sentiment Analysis
- Docker Deployment

---

# 👩‍💻 Author

**Ayesha Imran**

BS Artificial Intelligence

GitHub:
https://github.com/Ayesha1143

LinkedIn:
www.linkedin.com/in/ayesha-imran-a912a83b0

---

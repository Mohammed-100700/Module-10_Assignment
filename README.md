# 🩺 Heart Disease Prediction API

A simple FastAPI app that predicts the presence of heart disease using a trained machine learning model.
Focus: Dockerization and deployment to Render (not model accuracy).

---

## 🎯 Objective
- Train a basic model (e.g., Logistic Regression) on the Heart Disease dataset  
- Serve predictions with FastAPI  
- Dockerize and deploy to Render

---

## ⚙️ Setup & Installation

### 1) Create a virtual environment (optional but recommended)
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1      # Windows
    # source .venv/bin/activate       # macOS/Linux

### 2) Install dependencies
    pip install -r requirements.txt

### 3) Train the model
Download the dataset and save as heart.csv in the project folder:
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

Then run:
    python train_model.py

---

## 🚀 Run the application

### Run locally
    uvicorn app.main:app --reload
Open: http://127.0.0.1:8000/docs

### Run with Docker
    docker compose build
    docker compose up
Open: http://localhost:8000/docs

---

## 🧩 API Endpoints
- GET /health — health check  
- GET /info — model info & features  
- POST /predict — returns {"heart_disease": true|false}

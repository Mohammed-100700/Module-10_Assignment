🩺 Heart Disease Prediction API

A simple FastAPI app that predicts the presence of heart disease using a trained machine learning model.
This project focuses on Dockerization and deployment to Render.

🎯 Objective

Train a simple model (e.g., Logistic Regression) on the Heart Disease dataset.

Serve predictions using FastAPI.

Dockerize and deploy the app to Render.

⚙️ How to Run
1️⃣ Train the Model

Download the dataset from Kaggle:
https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset

Save it as heart.csv in your project folder.
Then run:

python train_model.py

2️⃣ Run Locally

uvicorn app.main:app --reload
Open the API docs: http://127.0.0.1:8000/docs

3️⃣ Run with Docker

docker compose build
docker compose up
Access docs at: http://localhost:8000/docs

# 🫁 Chronic Obstructive Pulmonary Disease (COPD) Prediction System

![COPD](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/COPD_Schematic.svg/640px-COPD_Schematic.svg.png)

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-0.24-orange?logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deploy-Render-brightgreen)](https://render.com/)

A **machine learning system** that predicts the likelihood of **Chronic Obstructive Pulmonary Disease (COPD)** in patients using clinical and lifestyle data.  
It helps in **early detection and risk assessment**, supporting healthcare professionals and patients in preventive care.

---

## 🔹 Features

- 🚀 **Predictive Analysis:** Estimates COPD risk based on patient data.  
- 🧠 **Machine Learning Models:** Uses **Gradient Boosting** and preprocessing pipelines for high accuracy.  
- 📊 **Data Handling:** Works with patient health records and asthma datasets.  
- 🌐 **Web Interface:** Simple form to input data and get instant predictions.  
- ☁️ **Deployment Ready:** Compatible with **Render**, **Heroku**, and other Python-supported platforms.  

---

## 🔹 Demo

![Demo GIF](https://media.giphy.com/media/3o7TKP9Y3XwCENQdU0/giphy.gif)  
*Example workflow: enter patient info → model predicts COPD risk → result displayed.*

---

## 🔹 Dataset

- `230patientsCOPD.csv` – Patient health records.  
- `asthma_dataset.csv` – Auxiliary dataset for preprocessing and analysis.  

> All datasets are preprocessed for machine learning.

---

## 🔹 Technology Stack

| Component         | Technology/Library                         |
|------------------|--------------------------------------------|
| Backend           | Python, FastAPI / Flask                     |
| Machine Learning  | scikit-learn (Gradient Boost, Pipelines)   |
| Data Handling     | pandas, numpy                              |
| Model Storage     | joblib, pickle                             |
| Frontend          | HTML (Jinja2 Templates)                    |
| Deployment        | Render / Heroku                             |

---

## 🔹 Project Structure

COPD-Prediction-System/
│
├── .ipynb_checkpoints/ # Jupyter notebook checkpoints
│ ├── 230patientsCOPD-checkpoint.csv
│ └── asthma_dataset-checkpoint.csv
│
├── anaconda_projects/
│ └── db/
│ └── project_filebrowser.db
│
├── models/ # Machine learning models
│ ├── full_pipeline.joblib
│ ├── full_pipeline.pkl
│ └── gradient_boost_model.pkl
│
├── templates/ # HTML frontend files
│ └── index.html
│
├── venv/ # Python virtual environment (ignored in git)
├── app.py # Main backend application
├── requirements.txt # Dependencies
└── README.md # Project documentation



---

## 🔹 How It Works

1. 📝 **Input Patient Data:** Enter patient info via the web form.  
2. ⚙️ **Data Preprocessing:** Data is cleaned, normalized, and encoded using pre-trained pipelines.  
3. 🤖 **Prediction:** Model predicts the probability of COPD.  
4. 📊 **Result Display:** Prediction shown in a **user-friendly interface**.

---

## 🔹 Installation & Setup

### 1️⃣ Clone the repository


git clone https://github.com/yourusername/COPD-Prediction-System.git
cd COPD-Prediction-System

2️⃣ Create a virtual environment and activate
python -m venv venv
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py
Access the app:

FastAPI: http://localhost:8000


🔹 Deployment
Deploy on Render, Heroku, or any Python-supported platform.

Use .env for environment variables like API keys or database URLs.

🔹 Future Enhancements
⏱ Real-time patient monitoring integration.

💡 Advanced ensemble models for higher accuracy.

🧾 Explainable AI (XAI) to interpret predictions.

📱 Mobile-friendly UI for better accessibility.


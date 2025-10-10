import os
import joblib
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd

app = FastAPI(title="COPD Prediction API")

# Setup Jinja2 templates (make sure you have templates/index.html)
templates = Jinja2Templates(directory="templates")

# ---------------------- LOAD PIPELINE ----------------------
PIPELINE_PATH = r"C:\Users\hp\OneDrive\Desktop\COPD Project Machine Learning\anaconda_projects\db\full_pipeline.joblib"

if os.path.exists(PIPELINE_PATH):
    pipeline = joblib.load(PIPELINE_PATH)
    print("✅ Pipeline loaded successfully!")
else:
    pipeline = None
    print(f"❌ Pipeline file not found at: {PIPELINE_PATH}")


# ---------------------- ROUTES ----------------------

# Show form page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Handle form submission


@app.post("/predict_form", response_class=HTMLResponse)
async def predict_form(
    request: Request,
    Age: int = Form(...),
    Gender: int = Form(...),
    BMI_kg_m2: float = Form(...),
    Height_m: float = Form(...),
    History_of_Heart_Failure: int = Form(...),
    Location: int = Form(...),
    working_place: int = Form(...),
    mMRC: int = Form(...),
    status_of_smoking: int = Form(...),
    Pack_History: int = Form(...),
    Vaccination: int = Form(...),
    Depression: int = Form(...),
    Dependent: int = Form(...),
    Temperature: float = Form(...),
    Respiratory_Rate: int = Form(...),
    Heart_Rate: int = Form(...),
    Blood_pressure: float = Form(...),
    Oxygen_Saturation: float = Form(...),
    Sputum: int = Form(...),
    FEV1: float = Form(...)
):
    if not pipeline:
        return templates.TemplateResponse("index.html", {"request": request, "result": "⚠️ Model not loaded"})

    # Build dataframe with feature names
    input_df = pd.DataFrame([{
        "Age": Age,
        "Gender": Gender,
        "BMI_kg_m2": BMI_kg_m2,
        "Height_m": Height_m,
        "History_of_Heart_Failure": History_of_Heart_Failure,
        "Location": Location,
        "working_place": working_place,
        "mMRC": mMRC,
        "status_of_smoking": status_of_smoking,
        "Pack_History": Pack_History,
        "Vaccination": Vaccination,
        "Depression": Depression,
        "Dependent": Dependent,
        "Temperature": Temperature,
        "Respiratory_Rate": Respiratory_Rate,
        "Heart_Rate": Heart_Rate,
        "Blood_pressure": Blood_pressure,
        "Oxygen_Saturation": Oxygen_Saturation,
        "Sputum": Sputum,
        "FEV1": FEV1
    }])

    # Prediction
    try:
        prediction = pipeline.predict(input_df)[0]
        result = f"Predicted Severity: {prediction}"
    except Exception as e:
        result = f"⚠️ Prediction failed: {str(e)}"

    return templates.TemplateResponse("index.html", {"request": request, "result": result})

from pydantic import BaseModel

class HeartData(BaseModel):
    age: int         # age in years
    sex: int         # 1=male, 0=female
    cp: int          # chest pain type (0-3)
    trestbps: int    # resting blood pressure
    chol: int        # serum cholestoral in mg/dl
    fbs: int         # fasting blood sugar > 120 mg/dl (1/0)
    restecg: int     # resting ECG results (0-2)
    thalach: int     # max heart rate achieved
    exang: int       # exercise induced angina (1/0)
    oldpeak: float   # ST depression induced by exercise
    slope: int       # slope of the peak exercise ST segment (0-2)
    ca: int          # number of major vessels (0-3)
    thal: int        # 0=unknown, 1=fixed, 2=normal, 3=reversible

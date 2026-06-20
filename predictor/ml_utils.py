import os
import joblib

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    'ml',
    'student_model.pkl'
)

METRICS_PATH = os.path.join(
    BASE_DIR,
    'ml',
    'model_metrics.pkl'
)

model = joblib.load(MODEL_PATH)
metrics = joblib.load(METRICS_PATH)
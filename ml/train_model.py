import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# Load dataset
data = pd.read_csv("C:\\Users\\ameen\\OneDrive\\Desktop\\StudentPerformancePredictor\\ml\\Final_Marks_Data.csv")

# Remove spaces from column names
data.columns = data.columns.str.strip()

# Features (input)
X = data[
    [
        'Attendance (%)',
        'Internal Test 1 (out of 40)',
        'Internal Test 2 (out of 40)',
        'Assignment Score (out of 10)',
        'Daily Study Hours'
    ]
]

# Target (output)
y = data['Final Exam Marks (out of 100)']

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
joblib.dump(model, 'student_model.pkl')

print("Model trained successfully.")
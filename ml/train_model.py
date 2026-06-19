import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    r2_score,
    mean_absolute_error,
    root_mean_squared_error
)

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)

print(f'R² Score: {r2:.2f}')
print(f'MAE: {mae:.2f}')
print(f'RMSE: {rmse:.2f}')
# Save model

feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': model.feature_importances_ * 100
})

feature_importance = feature_importance.sort_values(
    by='Importance',
    ascending=False
)

print(feature_importance)


joblib.dump(model, 'student_model.pkl')

metrics = {
    'r2_score': round(r2, 2),
    'mae': round(mae, 2),
    'rmse': round(rmse, 2),
    'feature_importance': feature_importance.to_dict(
        orient='records'
    )
}

joblib.dump(metrics, 'model_metrics.pkl')

print('Model and metrics saved successfully.')
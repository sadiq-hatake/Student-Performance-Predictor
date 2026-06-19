# Student Performance Predictor

A full-stack machine learning web application that predicts students' final exam marks based on attendance, internal assessment scores, assignment performance, and study habits.

Built using **Django, Scikit-Learn, SQLite, Pandas, and Bootstrap**.

---

## Features

* Add, edit, search, and delete student records
* Predict final exam marks using a trained machine learning model
* Generate personalized suggestions for improvement
* Display model evaluation metrics
* Visualize feature importance
* Dashboard with student analytics

---

## Machine Learning Workflow

```text
Dataset → Data Preprocessing → Model Training → Model Evaluation → Model Deployment → Real-Time Prediction
```

### Input Features

* Attendance (%)
* Internal Test 1 Score
* Internal Test 2 Score
* Assignment Score
* Daily Study Hours

### Target Variable

* Final Exam Marks (out of 100)

---

## Model Information

**Algorithm:** Random Forest Regressor

### Evaluation Metrics

* R² Score: **0.78**
* Mean Absolute Error (MAE): **4.16**
* Root Mean Squared Error (RMSE): **5.25**

### Feature Importance

| Feature           | Importance |
| ----------------- | ---------- |
| Attendance        | 42.83%     |
| Internal Test 2   | 23.65%     |
| Internal Test 1   | 23.49%     |
| Assignment Score  | 6.72%      |
| Daily Study Hours | 3.31%      |

### Key Insight

Attendance was identified as the most influential factor affecting student performance.

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Backend

* Django

### Machine Learning

* Scikit-Learn
* Pandas
* Joblib

### Database

* SQLite

---

## Project Structure

```text
StudentPerformancePredictor/
│
├── dataset/
│   └── Final_Marks_Data.csv
│
├── ml/
│   ├── train_model.py
│   ├── student_model.pkl
│   └── model_metrics.pkl
│
├── predictor/
│   ├── forms.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── ml_utils.py
│   └── templates/
│
├── studentpredictor/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sadiq-hatake/Student-Performance-Predictor.git
cd student-performance-predictor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Train the Machine Learning Model

```bash
cd ml
python train_model.py
cd ..
```

### 6. Run the Application

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Usage

1. Add student details.
2. Submit the form.
3. View the predicted score and personalized suggestions.
4. Monitor student analytics from the dashboard.
5. Search, edit, or delete records.

---

## Future Enhancements

* User authentication for students and teachers
* Interactive charts using Chart.js
* Export reports to PDF and CSV
* Compare multiple machine learning models
* Cloud deployment using Render or PythonAnywhere
* Email notifications for at-risk students

---

## Resume Description

Developed a full-stack Student Performance Predictor using Django and Random Forest Regression to estimate final exam marks based on attendance, internal assessments, assignments, and study habits. Achieved an R² score of 0.78 with a Mean Absolute Error (MAE) of 4.16 marks and identified attendance as the most influential factor through feature importance analysis.

---

## License

This project is intended for educational and learning purposes.

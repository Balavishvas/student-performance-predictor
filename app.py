from pathlib import Path

import pandas as pd
from flask import Flask, jsonify, render_template, request
from sklearn.linear_model import LinearRegression

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "student_data.csv"

FEATURES = [
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
]
TARGET = "exam_score"

app = Flask(__name__)


def train_model():
    df = pd.read_csv(DATA_PATH)
    model = LinearRegression()
    model.fit(df[FEATURES], df[TARGET])
    return model


model = train_model()


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/predict")
def predict():
    data = request.get_json(silent=True) or {}

    try:
        values = {
            "study_hours": float(data["study_hours"]),
            "attendance": float(data["attendance"]),
            "previous_score": float(data["previous_score"]),
            "assignments_completed": float(data["assignments_completed"]),
        }
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Please enter a value for every field."}), 400

    if not 0 <= values["attendance"] <= 100:
        return jsonify({"error": "Attendance must be between 0 and 100."}), 400
    if not 0 <= values["previous_score"] <= 100:
        return jsonify({"error": "Previous score must be between 0 and 100."}), 400
    if values["study_hours"] < 0 or values["assignments_completed"] < 0:
        return jsonify({"error": "Study hours and assignments cannot be negative."}), 400

    row = pd.DataFrame([values], columns=FEATURES)
    prediction = float(model.predict(row)[0])
    prediction = max(0.0, min(100.0, prediction))

    return jsonify({
        "prediction": round(prediction, 1),
        "label": performance_label(prediction),
    })


def performance_label(score):
    if score >= 85:
        return "Looking strong"
    if score >= 70:
        return "On a good track"
    if score >= 50:
        return "Room to improve"
    return "Needs attention"


if __name__ == "__main__":
    app.run(debug=True)

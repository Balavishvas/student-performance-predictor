from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "student_data.csv"

FEATURES = [
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
]
TARGET = "exam_score"


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    print("Student Performance Predictor")
    print("-" * 32)
    print(f"Mean Absolute Error : {mae:.2f}")
    print(f"Root Mean Squared Error: {rmse:.2f}")
    print(f"R² Score            : {r2:.2f}")

    sample_student = pd.DataFrame(
        [
            {
                "study_hours": 5.0,
                "attendance": 88,
                "previous_score": 76,
                "assignments_completed": 9,
            }
        ]
    )
    predicted_score = model.predict(sample_student)[0]
    print(f"\nPredicted exam score: {predicted_score:.1f}")

    plt.figure(figsize=(7, 5))
    plt.scatter(y_test, predictions)
    plt.xlabel("Actual Exam Score")
    plt.ylabel("Predicted Exam Score")
    plt.title("Actual vs Predicted Exam Scores")
    plt.plot([y.min(), y.max()], [y.min(), y.max()])
    plt.tight_layout()
    plt.savefig(ROOT / "actual_vs_predicted.png", dpi=150)
    print("\nSaved chart: actual_vs_predicted.png")


if __name__ == "__main__":
    main()

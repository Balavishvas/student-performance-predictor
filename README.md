# Student Performance Predictor

A small machine-learning project that predicts a student's exam score using academic and study-related features.

## What it uses

The model learns from four inputs:

- Study hours
- Attendance percentage
- Previous exam score
- Number of assignments completed

The target is the student's final exam score.

## Machine Learning Workflow

1. Load the student dataset with Pandas.
2. Separate features and target.
3. Split the data into training and testing sets.
4. Train a Linear Regression model using scikit-learn.
5. Predict scores for unseen test data.
6. Evaluate the model using MAE, RMSE, and R².
7. Generate an Actual vs Predicted visualization.

## Project Structure

```text
student-performance-predictor/
├── data/
│   └── student_data.csv
├── src/
│   └── train_model.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Balavishvas/student-performance-predictor.git
cd student-performance-predictor
pip install -r requirements.txt
```

## Run

```bash
python src/train_model.py
```

The program prints the model evaluation metrics and a prediction for a sample student. It also saves an `actual_vs_predicted.png` chart locally.

## Example Prediction

The script includes an example student with:

```text
Study hours: 5
Attendance: 88%
Previous score: 76
Assignments completed: 9
```

The trained model estimates the student's final exam score from these values.

## Technologies

Python · Pandas · Scikit-learn · Matplotlib · Linear Regression

## Learning Goals

This project demonstrates a complete beginner-friendly supervised machine-learning pipeline: dataset preparation, feature selection, train/test splitting, regression training, evaluation, prediction, and visualization.

## Note

The included dataset is a small synthetic dataset created for learning and demonstration. Predictions should not be interpreted as real educational assessments.

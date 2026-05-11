Insurance Purchase Prediction using Logistic Regression

Project Overview

This project predicts whether a person may buy insurance based on their age using the:

 Logistic Regression Algorithm

The model is trained using a small insurance dataset and visualizes the:

* Logistic Regression Sigmoid Curve
* Probability Predictions
* Decision Boundary

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

---

# Machine Learning Type

This project is a:

# Binary Classification Problem

Because the target column contains:

| bought_insurance |
| ---------------- |
| 0                |
| 1                |

Where:

* `0` → Person will not buy insurance
* `1` → Person will buy insurance

---

# Dataset Information

Dataset File:

```text id="d0q8s0"
insurance_data.csv
```

Dataset Columns:

| Column           | Description   |
| ---------------- | ------------- |
| age              | Person age    |
| bought_insurance | Target output |

---

# Project Workflow

```text id="2f2r6r"
Load Dataset
    ↓
Feature Selection
    ↓
Train-Test Split
    ↓
Model Training
    ↓
Prediction
    ↓
Accuracy Evaluation
    ↓
Sigmoid Curve Visualization
```

---

# Logistic Regression

The project uses:

# Logistic Regression

because the output is:

```text id="zjlwm0"
0 or 1
```

This algorithm predicts probabilities between:

```text id="b68wxh"
0 to 1
```

using the sigmoid function.

---

# Sigmoid Function

Logistic Regression uses:

\sigma(x)=\frac{1}{1+e^{-x}}

This creates the:

# S-shaped sigmoid curve

---

# Visualization

The project visualizes:

* Actual dataset points using scatter plot
* Logistic Regression sigmoid curve
* 0.5 decision threshold line

---

# Important Visualization Logic

The sigmoid curve is generated using:

```python id="2gl6po"
model.predict_proba()
```

which returns probability values.

Example:

| Age | Probability |
| --- | ----------- |
| 22  | 0.10        |
| 35  | 0.55        |
| 50  | 0.95        |

---

# Model Accuracy

Accuracy is calculated using:

```python id="8uvfx0"
accuracy_score()
```

This checks how well the model predicts unseen data.

---

# Example Prediction

Input:

```python id="qcsn7y"
[[35]]
```

Output:

```text id="e5a4yo"
[1]
```

Meaning:

```text id="b5rg1j"
Person may buy insurance
```

---

# Features of This Project

* Logistic Regression Training
* Binary Classification
* Train-Test Split
* Accuracy Evaluation
* Sigmoid Curve Visualization
* Probability Prediction
* Decision Threshold Visualization

---

# Learning Outcomes

Through this project, you can learn:

* Machine Learning workflow
* Logistic Regression
* Binary Classification
* Sigmoid Function
* Probability Prediction
* Data Visualization with Matplotlib
* Model Accuracy Evaluation

---

# Future Improvements

* Add more features such as salary, city, or medical history
* Compare Logistic Regression with other ML algorithms
* Build a Flask Web App
* Deploy using Streamlit
* Use larger real-world insurance datasets

---

# Author
 TEAM :
     Nexus Forge

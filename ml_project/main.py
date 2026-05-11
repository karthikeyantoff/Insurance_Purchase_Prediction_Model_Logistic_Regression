import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load dataset
df = pd.read_csv("data_sets\insurance_data.csv")

# 2. Setup Input and Output
X = df[['age']]
y = df['bought_insurance']

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Create and Train Model
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Predictions & Accuracy
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# -------------------------------------------------
# VISUALIZATION (The Correct Way)
# -------------------------------------------------

# Scatter plot of actual data points
plt.scatter(X, y, color='blue', marker='+', label='Actual Data')

# Generate 100 points between min and max age for a smooth curve
X_smooth = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)

# Get the probabilities for class 1 (Bought Insurance)
y_probs = model.predict_proba(X_smooth)[:, 1]

# Plot the Sigmoid Curve
plt.plot(X_smooth, y_probs, color='red', label='Logistic Curve')

# Optional: Add the 0.5 Decision Threshold line
plt.axhline(y=0.5, color='gray', linestyle='--', label='0.5 Threshold')

plt.xlabel("Age")
plt.ylabel("Probability of Buying Insurance")
plt.title("Insurance Purchase Prediction")
plt.legend()
plt.show()

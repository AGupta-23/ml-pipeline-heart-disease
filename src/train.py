# src/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
df = pd.read_csv("../data/heart.csv")

# Step 2: Split features (X) and target (y)
X = df.drop("output", axis=1)   # all columns except output
y = df["output"]                # target column

# Step 3: Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train model (Logistic Regression is good for classification)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 5: Predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate
acc = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {acc:.2f}")

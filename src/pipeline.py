import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.linear_model import LogisticRegression

def load_data(path="../data/heart.csv"):
    return pd.read_csv(path)

# simple feature engineering: chol/fbs ratio
def add_feature(X):
    X = X.copy()
    X["chol_fbs_ratio"] = X["chol"] / (X["fbs"] + 1)
    return X

def build_pipeline():
    num_cols = ["age", "trestbps", "chol", "thalach", "oldpeak", "chol_fbs_ratio"]
    cat_cols = ["sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal"]

    num_pipe = Pipeline([
        ("scaler", StandardScaler())
    ])

    cat_pipe = Pipeline([
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_pipe, num_cols),
        ("cat", cat_pipe, cat_cols)
    ])

    model = LogisticRegression(max_iter=1000)

    pipe = Pipeline([
        ("feat", FunctionTransformer(add_feature)),
        ("prep", preprocessor),
        ("clf", model)
    ])

    return pipe

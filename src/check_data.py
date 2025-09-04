import pandas as pd

df = pd.read_csv("../data/heart.csv")
print("Columns:", df.columns.tolist())
print(df.head())

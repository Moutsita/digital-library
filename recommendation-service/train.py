import pandas as pd
import joblib
import os

os.makedirs("model", exist_ok=True)

# dataset: user_id, book_id

df = pd.read_csv("data/loans_clean.csv")

recommendations = {}

for user_id in df["user_id"].unique():
    popular_books = (
        df.groupby("book_id")
        .size()
        .sort_values(ascending=False)
        .head(5)
        .index
        .tolist()
    )
    recommendations[int(user_id)] = popular_books

joblib.dump(recommendations, "model/model.pkl")
print("Model saved")
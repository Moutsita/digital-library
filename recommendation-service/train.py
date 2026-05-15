# import pandas as pd
# import joblib
# import os

# os.makedirs("model", exist_ok=True)

# # dataset: user_id, book_id

# df = pd.read_csv("data/loans_clean.csv")

# recommendations = {}

# for user_id in df["user_id"].unique():
#     popular_books = (
#         df.groupby("book_id")
#         .size()
#         .sort_values(ascending=False)
#         .head(5)
#         .index
#         .tolist()
#     )
#     recommendations[int(user_id)] = popular_books

# joblib.dump(recommendations, "model/model.pkl")
# print("Model saved")

import pandas as pd
import joblib
import os

# Créer le dossier recommendation-service/model
os.makedirs("recommendation-service/model", exist_ok=True)

# Charger les données prétraitées
df = pd.read_csv("data/loans_clean.csv")

# Dictionnaire simple de recommandations
recommendations = {}

# Livres les plus populaires
popular_books = (
    df.groupby("book_id")
    .size()
    .sort_values(ascending=False)
    .head(5)
    .index
    .tolist()
)

# Même recommandation pour chaque utilisateur
for user_id in df["user_id"].unique():
    recommendations[int(user_id)] = popular_books

# Sauvegarde du modèle
joblib.dump(
    recommendations,
    "recommendation-service/model/model.pkl"
)

print("Model saved")
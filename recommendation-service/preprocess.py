import pandas as pd
import os

os.makedirs("data", exist_ok=True)

# lecture du dataset brut

df = pd.read_csv("data/loans.csv")

# suppression des doublons

df = df.drop_duplicates()

# suppression des valeurs nulles

df = df.dropna()

# sauvegarde

df.to_csv("data/loans_clean.csv", index=False)

print("Preprocessing completed")
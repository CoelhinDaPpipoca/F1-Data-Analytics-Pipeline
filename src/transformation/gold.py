import pandas as pd
import os

print("Gerando camada Gold...")

df = pd.read_csv(
    "data/silver/f1_clean.csv"
)

gold = df.copy()

gold = gold.sort_values(

    "points",

    ascending=False

)

os.makedirs(

    "data/gold",

    exist_ok=True

)

gold.to_csv(

    "data/gold/dashboard.csv",

    index=False

)

print(
    gold.head()
)
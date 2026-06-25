import pandas as pd
import os

print("Iniciando transformação...")

arquivo = "data/bronze/f1_raw.csv"

df = pd.read_csv(arquivo)

# limpeza básica

df = df.drop_duplicates()

df = df.dropna()

os.makedirs(
    "data/silver",
    exist_ok=True
)

df.to_csv(
    "data/silver/f1_clean.csv",
    index=False
)

print("Transformação concluída")
print(df.head())
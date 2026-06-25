import pandas as pd
import os

print("Iniciando ingestão...")

origem = "data/sample_f1_data.csv"

df = pd.read_csv(
    origem
)

os.makedirs(
    "data/bronze",
    exist_ok=True
)

destino = (
    "data/bronze/f1_raw.csv"
)

df.to_csv(
    destino,
    index=False
)

print(
    "Ingestão concluída"
)

print(
    f"Registros carregados: {len(df)}"
)
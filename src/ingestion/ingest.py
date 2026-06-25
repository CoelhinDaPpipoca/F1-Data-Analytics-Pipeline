import shutil
import os

print("Iniciando ingestão...")

origem = "data/bronze/sample_f1_data.csv"

destino = "data/bronze/f1_raw.csv"

os.makedirs(
    "data/bronze",
    exist_ok=True
)

shutil.copy(
    origem,
    destino
)

print("Ingestão concluída")
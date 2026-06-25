import pandas as pd
import os

print("Gerando camada Gold...")

df = pd.read_csv(
    "data/silver/f1_clean.csv"
)

# agregação automática baseada nas colunas

colunas = list(df.columns)

if len(colunas) >= 2:

    gold = (
        df
        .groupby(
            colunas[0]
        )
        .size()
        .reset_index(
            name="quantidade"
        )
    )

else:

    gold = df.copy()

os.makedirs(
    "data/gold",
    exist_ok=True
)

gold.to_csv(
    "data/gold/dashboard.csv",
    index=False
)

print("Gold concluído")
print(gold.head())
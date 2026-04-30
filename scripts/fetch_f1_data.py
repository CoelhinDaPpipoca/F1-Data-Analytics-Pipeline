import pandas as pd

# Simulando dados de corrida (como se viessem de uma API)
data = {
    "driver": ["Verstappen", "Hamilton", "Leclerc", "Norris"],
    "team": ["Red Bull", "Mercedes", "Ferrari", "McLaren"],
    "position": [1, 2, 3, 4],
    "laps": [58, 58, 58, 58],
    "time_seconds": [5400, 5420, 5450, 5480]
}

# Criando DataFrame
df = pd.DataFrame(data)

# Salvando como CSV
df.to_csv("data/sample_f1_data.csv", index=False)

print("Dados salvos em data/sample_f1_data.csv")

import pandas as pd

df = pd.read_csv("data/bank_transactions.csv")
df.sample(5000, random_state=42).to_csv("data/muestra_transacciones.csv", index=False)
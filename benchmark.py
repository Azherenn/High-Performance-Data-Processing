import sqlite3
import pandas as pd
import time

conn = sqlite3.connect('sales.db')
df = pd.read_sql_query("SELECT * FROM sales", conn)
conn.close()
print(f"Dados carregados: {len(df)} linhas.")

inicio = time.perf_counter()

p_media = df['value'].mean()
p_max   = df['value'].max()
p_min   = df['value'].min()
p_total = df['value'].sum()

fim = time.perf_counter()

time_python = fim - inicio

print(f"🐢 Python levou: {time_python:.6f} segundos")
print(f"Check: Média={p_media:.2f}, Max={p_max}, Min={p_min}")
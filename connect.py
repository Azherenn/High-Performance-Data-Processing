import sqlite3
import pandas as pd
import numpy as np
import ctypes

conn = sqlite3.connect('sales.db')
df = pd.read_sql_query("SELECT * FROM sales", conn)
conn.close()

prices_list = df['value'].tolist()
prices_list_array = np.array(prices_list)
print(prices_list_array)
lib = ctypes.CDLL("./libprocessor.so")
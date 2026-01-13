import sqlite3
import pandas as pd
import time
import ctypes
import platform
import os

print("loading data from the database")
try:
    conn = sqlite3.connect('sales.db')
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    print(f"Data loaded: {len(df)} records.")
except Exception as e:
    print(f"Error reading bank: {e}")
    exit()

sistema = platform.system()
lib_name = ""

if sistema == "Windows":
    lib_name = "./sales_lib.dll"
elif sistema == "Linux":
    lib_name = "./libsales.so"
else:
    lib_name = "./libsales.so"

print(f"🔧 System detected: {sistema}. Searching for: {lib_name}")

if not os.path.exists(lib_name):
    print(f"ECRITICAL ERROR: The file '{lib_name}' not found!")
    print("Did you remember to compile the C code before running it?")
    exit()

lib = ctypes.CDLL(lib_name)

c_double_p = ctypes.POINTER(ctypes.c_double)

lib.calcular_media.restype = ctypes.c_double
lib.calcular_media.argtypes = [c_double_p, ctypes.c_int]

lib.calcular_total.restype = ctypes.c_double
lib.calcular_total.argtypes = [c_double_p, ctypes.c_int]

lib.maior_venda.restype = ctypes.c_double
lib.maior_venda.argtypes = [c_double_p, ctypes.c_int]

lib.menor_venda.restype = ctypes.c_double
lib.menor_venda.argtypes = [c_double_p, ctypes.c_int]

lib.desvio_padrao.restype = ctypes.c_double
lib.desvio_padrao.argtypes = [c_double_p, ctypes.c_int]

lib.vendas_premium.restype = ctypes.c_int
lib.vendas_premium.argtypes = [c_double_p, ctypes.c_int, ctypes.c_double]

inicio_conv = time.perf_counter()

valores_python = df['value'].to_list()
array_type = ctypes.c_double * len(valores_python)
c_array = array_type(*valores_python)
tamanho = len(valores_python)

fim_conv = time.perf_counter()
print(f"✅ Conversion completed in {fim_conv - inicio_conv:.4f}s")

print("\n--- Starting Python Benchmark (PANDAS/NUMPY) ---")
start_py = time.perf_counter()

py_media = df['value'].mean()
py_total = df['value'].sum()
py_max   = df['value'].max()
py_min   = df['value'].min()
py_std   = df['value'].std()

py_prem  = len(df[df['value'] >= 3000])

end_py = time.perf_counter()
tempo_py = end_py - start_py
print(f"Python Time: {tempo_py:.6f} seconds")

print("\n---STARTING BENCHMARK C (DLL) ---")
start_c = time.perf_counter()

c_media = lib.calcular_media(c_array, tamanho)
c_total = lib.calcular_total(c_array, tamanho)
c_max   = lib.maior_venda(c_array, tamanho)
c_min   = lib.menor_venda(c_array, tamanho)
c_std   = lib.desvio_padrao(c_array, tamanho)
c_prem  = lib.vendas_premium(c_array, tamanho, 3000.0)

end_c = time.perf_counter()
tempo_c = end_c - start_c
print(f"C time: {tempo_c:.6f} seconds")

print("\n========================================")
print("FINAL SCOREBOARD")
print("========================================")
print(f"Python: {tempo_py:.6f}s")
print(f"C DLL : {tempo_c:.6f}s")

fator = tempo_py / tempo_c if tempo_c > 0 else 0
print(f"\nThe C code was {fator:.2f}x Faster than Python!")

print("\n--- CHECKING VALUES (Validating if the account matches) ---")
print(f"Average -> Py: {py_media:.2f} | C: {c_media:.2f}")
print(f"Total  -> Py: {py_total:.2f} | C: {c_total:.2f}")
print(f"Detour -> Py: {py_std:.2f} | C: {c_std:.2f}")
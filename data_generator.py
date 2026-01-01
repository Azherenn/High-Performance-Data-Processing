import sqlite3
import random
from datetime import datetime, timedelta

connector = sqlite3.connect('sales.db')
cursor = connector.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        value REAL NOT NULL,
        date TEXT NOT NULL
    )
''')

connector.commit()
print("Table 'sales' successfully verified/created!")

product = ['Carne bovina', 'carne suína', 'Ovo', 'Leite', 'Azeite', 'Tomate', 'Alface', 'Fígado', 'Beringela', 'Feijão']
product_fake = []

now = datetime.now()

for i in range(1000000):
    randomized_product = random.choice(product)
    price = random.uniform(50.0, 5000.0)
    random_days = random.randint(0, 365)
    sale_date = now - timedelta(days=random_days)
    date_str = sale_date.strftime("%Y-%m-%d %H:%M:%S")
    new_product = (randomized_product, price, date_str)
    product_fake.append(new_product)

sql_insert = "INSERT INTO sales (product, value, date) VALUES (?, ?, ?)"
cursor.executemany(sql_insert, product_fake)

connector.commit()

connector.close()
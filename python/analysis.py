import pandas as pd
import sqlite3


# csv cu encoding corect
df = pd.read_csv(r"D:/sales-analysis-project/data/sales.csv", encoding='ISO-8859-1')

#creare baza sqlite
conn = sqlite3.connect(r"D:/sales-analysis-project/data/sales.db")
#scriere dataset clean in tabelsql
df.to_sql("sales", conn, if_exists="replace", index=False)

# primele 5 r
print(df.head())

# inf despre coloane tipuri
print(df.info())

# valori lipsa
print(df.isnull().sum())

df = df.drop_duplicates()

print(df.isnull().sum())
df=df.dropna()

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df.columns)

df.to_csv(r"D:/sales-analysis-project/data/sales_clean.csv", index=False, encoding='ISO-8859-1')

# randuri totale
query = "SELECT COUNT(*) AS total_rows FROM sales"
print(pd.read_sql(query, conn))

# vanzari totale
query = "SELECT SUM(Sales) AS total_sales FROM sales"
print(pd.read_sql(query, conn))

# vanzare pe regiune
query = """
SELECT Region, SUM(Sales) AS total_sales
FROM sales
GROUP BY Region
ORDER BY total_sales DESC
"""
print(pd.read_sql(query, conn))

# top 10 produse in functie de vanzare
query = """
SELECT "Product Name", SUM(Sales) AS total_sales
FROM sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 10
"""
print(pd.read_sql(query, conn))

# vanzare pe luna
query = """
SELECT strftime('%Y-%m', "Order Date") AS month, SUM(Sales) AS total_sales
FROM sales
GROUP BY month
ORDER BY month
"""
print(pd.read_sql(query, conn))

# profit pe categorie
query = """
SELECT Category, SUM(Profit) AS total_profit
FROM sales
GROUP BY Category
ORDER BY total_profit DESC
"""
print(pd.read_sql(query, conn))
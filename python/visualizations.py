import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"D:/sales-analysis-project/data/sales_clean.csv", encoding='ISO-8859-1')
df["Order Date"] = pd.to_datetime(df["Order Date"])

#vanzari totale pe regiune

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.index, y=region_sales.values, palette="Blues_d")
plt.title("Total Sales by Region")
plt.ylabel("Total Sales")
plt.xlabel("Region")
plt.savefig(r"D:/sales-analysis-project/dashboard/region_sales.png", dpi=300, bbox_inches='tight')
plt.show()

#top10 produse dupa vanzari

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette="Greens_d")
plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.savefig(r"D:/sales-analysis-project/dashboard/top_products.png", dpi=300, bbox_inches='tight')
plt.show()

#vanzari lunare

df["Order Date"] = pd.to_datetime(df["Order Date"])
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.savefig(r"D:/sales-analysis-project/dashboard/monthly_sales.png", dpi=300, bbox_inches='tight')
plt.show()

#profit pe categorie

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
sns.barplot(x=category_profit.index, y=category_profit.values, palette="Oranges_d")
plt.title("Profit by Category")
plt.ylabel("Total Profit")
plt.xlabel("Category")
plt.savefig(r"D:/sales-analysis-project/dashboard/profit_category.png", dpi=300, bbox_inches='tight')
plt.show()
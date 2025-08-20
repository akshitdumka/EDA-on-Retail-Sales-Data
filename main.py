# 📦 Importing Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 📂 Set Working Directory (Optional if running from same folder)
os.chdir(r"C:\Users\10112\OneDrive\Desktop\Exploratory Data Analysis")

# 📥 Load the Datasets
df_sales = pd.read_csv("mock_kaggle.csv")
df_menu = pd.read_csv("menu.csv")

# 📌 Display first few rows
print("📊 Sales Dataset:")
print(df_sales.head(), "\n")

print("📋 Menu Dataset:")
print(df_menu.head(), "\n")

# 🧼 Data Cleaning for Sales Dataset
def clean_sales(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df.dropna(how='all', inplace=True)
    df.drop_duplicates(inplace=True)
    return df

# 🧼 Data Cleaning for Menu Dataset
def clean_menu(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    df.dropna(how='all', inplace=True)
    df.drop_duplicates(inplace=True)
    return df

df_sales = clean_sales(df_sales)
df_menu = clean_menu(df_menu)

# ✅ Check for missing values
print("\n🧹 Missing Values in Sales:")
print(df_sales.isnull().sum())

print("\n🧹 Missing Values in Menu:")
print(df_menu.isnull().sum())

# 📊 Basic Descriptive Statistics
print("\n📈 Sales Dataset Summary:")
print(df_sales.describe(include='all'))

print("\n📈 Menu Dataset Summary:")
print(df_menu.describe(include='all'))

# ✅ Calculate total revenue amount per row
df_sales['amount'] = df_sales['venda'] * df_sales['preco']

# ✅ Now this will work
sns.histplot(df_sales['amount'], kde=True)
plt.title('Distribution of Sales Amount')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.show()

# Basic stats for numerical columns
print("Mean:\n", df.mean(numeric_only=True))
print("Median:\n", df.median(numeric_only=True))
print("Mode:\n", df.mode(numeric_only=True).iloc[0])
print("Standard Deviation:\n", df.std(numeric_only=True))
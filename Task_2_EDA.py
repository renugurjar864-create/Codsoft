import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_csv('customer_sales_data (9).csv')

# Dataset Summary
print("Data Shape:", df.shape)
print("\n--- Summary Statistics ---")
print(df.describe())

# Data Cleaning
df.drop_duplicates(inplace=True)
print("\nMissing Values:\n", df.isnull().sum())

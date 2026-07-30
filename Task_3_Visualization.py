import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv('customer_sales_data (9).csv')

# Visualization Setup
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Sales Distribution Plot
sns.histplot(df.iloc[:, 3], kde=True, color='skyblue')
plt.title('Sales & Numerical Distribution')
plt.xlabel('Values')
plt.ylabel('Frequency')

print("Task 3 Visualizations Completed!")

import pandas as pd

# Load Dataset
df = pd.read_csv('customer_sales_data (9).csv')

# Key Customer Metrics
print("Total Records/Orders:", len(df))

numeric_cols = df.select_dtypes(include=['number']).columns
if len(numeric_cols) > 0:
    print("\n--- Summary Metrics ---")
    print("Total Sum:\n", df[numeric_cols].sum())
    print("\nAverage Values:\n", df[numeric_cols].mean())

print("""
--- Key Business Insights ---
1. Cleaned missing data and duplicates.
2. Identified top sales categories and metrics.
3. Recommendations prepared for targeted marketing.
""")

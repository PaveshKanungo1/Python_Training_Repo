import pandas as pd

df = pd.read_csv('sales_data.csv')

df['Total_Sale'] = df['Quantity'] * df['Price']

total_sales = df['Total_Sale'].sum()

average_sales = df['Total_Sale'].mean()

top_selling_product = df.groupby('Product')['Quantity'].sum().idxmax()

print(f"Total Sales: ${total_sales:.2f}")
print(f"Average Sales per Transaction: ${average_sales:.2f}")
print(f"Top-Selling Product: {top_selling_product}")
import pandas as pd

# Inbuilt mock sales data (at least 10 rows)
data = [
    {'Date': '2025-07-01', 'Product': 'Laptop', 'Units Sold': 3, 'Revenue': 3000},
    {'Date': '2025-07-02', 'Product': 'Mouse', 'Units Sold': 10, 'Revenue': 500},
    {'Date': '2025-07-03', 'Product': 'Keyboard', 'Units Sold': 5, 'Revenue': 750},
    {'Date': '2025-07-04', 'Product': 'Monitor', 'Units Sold': 2, 'Revenue': 4000},
    {'Date': '2025-07-05', 'Product': 'Printer', 'Units Sold': 1, 'Revenue': 2500},
    {'Date': '2025-07-06', 'Product': 'Mouse', 'Units Sold': 7, 'Revenue': 350},
    {'Date': '2025-07-07', 'Product': 'Laptop', 'Units Sold': 2, 'Revenue': 2000},
    {'Date': '2025-07-08', 'Product': 'Monitor', 'Units Sold': 1, 'Revenue': 2000},
    {'Date': '2025-07-09', 'Product': 'Keyboard', 'Units Sold': 4, 'Revenue': 600},
    {'Date': '2025-07-10', 'Product': 'Printer', 'Units Sold': 2, 'Revenue': 4800},
    {'Date': '2025-07-11', 'Product': 'Laptop', 'Units Sold': 1, 'Revenue': 1500},
    {'Date': '2025-07-12', 'Product': 'Mouse', 'Units Sold': 12, 'Revenue': 600}
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('data.csv', index=False)

print("✅ 'data.csv' created with mock sales data!")

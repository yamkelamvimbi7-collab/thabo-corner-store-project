from data_cleaning import (
    load_raw_data,
    clean_products,
    clean_sales,
    cleaning_summary,
)

# Load the raw CSV files
products_raw, sales_raw = load_raw_data(
    "data/products.csv",
    "data/sales.csv",
)

# Clean the products first
products_clean = clean_products(products_raw)

# Use cleaned product IDs to validate sales
sales_clean = clean_sales(
    sales_raw,
    products_clean["product_id"].dropna().unique(),
)

# Display the results
print(cleaning_summary(products_raw, products_clean, "products"))
print(cleaning_summary(sales_raw, sales_clean, "sales"))

print("\n--- Cleaned products (first 5 rows) ---")
print(products_clean.head())

print("\n--- Cleaned sales (first 5 rows) ---")
print(sales_clean.head())

print("\n--- Missing values in cleaned products ---")
print(products_clean.isna().sum())

print("\n--- Missing values in cleaned sales ---")
print(sales_clean.isna().sum())

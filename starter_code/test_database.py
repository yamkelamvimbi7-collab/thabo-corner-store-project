from data_cleaning import (
    load_raw_data,
    clean_products,
    clean_sales,
)

from database import (
    get_connection,
    create_tables,
    insert_products,
    insert_sales,
    query_total_revenue_per_product,
    query_best_selling_product,
    query_sales_by_payment_method,
    query_custom_one,
    query_custom_two,
)


# Load and clean the CSV files.
products_raw, sales_raw = load_raw_data(
    "data/products.csv",
    "data/sales.csv",
)

products_clean = clean_products(products_raw)

sales_clean = clean_sales(
    sales_raw,
    products_clean["product_id"].dropna().unique(),
)

# Create the database and tables.
conn = get_connection("store.db")

try:
    create_tables(conn)

    # Insert the cleaned data.
    insert_products(conn, products_clean)
    insert_sales(conn, sales_clean)

    # Check the number of records.
    print("Products in database:",
          conn.execute("SELECT COUNT(*) FROM products").fetchone()[0])

    print("Sales in database:",
          conn.execute("SELECT COUNT(*) FROM sales").fetchone()[0])

    # Run the five SQL queries.
    queries = [
        ("Revenue per product",
         query_total_revenue_per_product),
        ("Best-selling product",
         query_best_selling_product),
        ("Sales by payment method",
         query_sales_by_payment_method),
        ("Revenue by category",
         query_custom_one),
        ("Monthly revenue",
         query_custom_two),
    ]

    for title, query_function in queries:
        print(f"\n--- {title} ---")
        for row in query_function(conn):
            print(row)

    # Verify foreign-key relationships.
    invalid_sales = conn.execute("""
        SELECT COUNT(*)
        FROM sales AS s
        LEFT JOIN products AS p
            ON s.product_id = p.product_id
        WHERE p.product_id IS NULL
    """).fetchone()[0]

    print("\nSales with invalid product references:",
          invalid_sales)

finally:
    conn.close()

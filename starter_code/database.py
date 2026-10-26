
"""
database.py
------------
Task 3: Build a relational database from cleaned data.
"""

import sqlite3


def get_connection(db_path: str = "store.db") -> sqlite3.Connection:
    """Open or create the SQLite database."""

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_tables(conn: sqlite3.Connection) -> None:
    """Create related products and sales tables."""

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT NOT NULL,
            category TEXT,
            unit_price REAL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            sale_id TEXT PRIMARY KEY,
            product_id TEXT,
            quantity INTEGER,
            sale_date TEXT,
            payment_method TEXT,
            customer_type TEXT,
            FOREIGN KEY (product_id)
                REFERENCES products(product_id)
        )
    """)

    conn.commit()


def insert_products(conn: sqlite3.Connection, products_df) -> None:
    """Insert cleaned products into the database."""

    columns = [
        "product_id",
        "product_name",
        "category",
        "unit_price",
    ]

    products = products_df[columns]

    sql = """
        INSERT OR REPLACE INTO products
        (product_id, product_name, category, unit_price)
        VALUES (?, ?, ?, ?)
    """

    rows = [
        tuple(None if value is None else value
              for value in row)
        for row in products.itertuples(index=False, name=None)
    ]

    conn.executemany(sql, rows)
    conn.commit()


def insert_sales(conn: sqlite3.Connection, sales_df) -> None:
    """Insert cleaned sales into the database."""

    columns = [
        "sale_id",
        "product_id",
        "quantity",
        "sale_date",
        "payment_method",
        "customer_type",
    ]

    sales = sales_df[columns]

    sql = """
        INSERT OR REPLACE INTO sales
        (sale_id, product_id, quantity, sale_date,
         payment_method, customer_type)
        VALUES (?, ?, ?, ?, ?, ?)
    """

    rows = [
        tuple(None if value is None else value
              for value in row)
        for row in sales.itertuples(index=False, name=None)
    ]

    conn.executemany(sql, rows)
    conn.commit()


def query_total_revenue_per_product(conn: sqlite3.Connection):
    """Return each product's revenue, highest first."""

    sql = """
        SELECT
            p.product_name,
            SUM(s.quantity * p.unit_price) AS total_revenue
        FROM products AS p
        JOIN sales AS s
            ON p.product_id = s.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_revenue DESC
    """

    return conn.execute(sql).fetchall()


def query_best_selling_product(conn: sqlite3.Connection):
    """Return the product with the highest quantity sold."""

    sql = """
        SELECT
            p.product_name,
            SUM(s.quantity) AS total_quantity
        FROM products AS p
        JOIN sales AS s
            ON p.product_id = s.product_id
        GROUP BY p.product_id, p.product_name
        ORDER BY total_quantity DESC
        LIMIT 1
    """

    return conn.execute(sql).fetchall()


def query_sales_by_payment_method(conn: sqlite3.Connection):
    """Count transactions for each payment method."""

    sql = """
        SELECT
            payment_method,
            COUNT(*) AS transaction_count
        FROM sales
        GROUP BY payment_method
        ORDER BY transaction_count DESC
    """

    return conn.execute(sql).fetchall()


def query_custom_one(conn: sqlite3.Connection):
    """
    Business question:
    Which product category generates the most revenue?
    """

    sql = """
        SELECT
            p.category,
            SUM(s.quantity * p.unit_price) AS total_revenue
        FROM products AS p
        JOIN sales AS s
            ON p.product_id = s.product_id
        GROUP BY p.category
        ORDER BY total_revenue DESC
    """

    return conn.execute(sql).fetchall()


def query_custom_two(conn: sqlite3.Connection):
    """
    Business question:
    What is the total revenue for each month?
    """

    sql = """
        SELECT
            substr(sale_date, 1, 7) AS sales_month,
            SUM(s.quantity * p.unit_price) AS monthly_revenue
        FROM sales AS s
        JOIN products AS p
            ON s.product_id = p.product_id
        GROUP BY substr(sale_date, 1, 7)
        ORDER BY sales_month
    """

    return conn.execute(sql).fetchall()

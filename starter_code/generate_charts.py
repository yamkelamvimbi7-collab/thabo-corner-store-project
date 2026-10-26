
import sqlite3

from visualize import (
    bar_chart_revenue_per_product,
    line_chart_monthly_trend
)

# Connect to the store database in the project folder.
conn = sqlite3.connect("store.db")

# Get total revenue for each product.
revenue_rows = conn.execute("""
    SELECT p.product_name,
           SUM(p.unit_price * s.quantity)
    FROM sales s
    JOIN products p ON p.product_id = s.product_id
    GROUP BY p.product_name
    ORDER BY SUM(p.unit_price * s.quantity) DESC
""").fetchall()

# Get total units sold in each month.
monthly_rows = conn.execute("""
    SELECT SUBSTR(s.sale_date, 1, 7),
           SUM(s.quantity)
    FROM sales s
    GROUP BY SUBSTR(s.sale_date, 1, 7)
    ORDER BY SUBSTR(s.sale_date, 1, 7)
""").fetchall()

conn.close()

# Prepare data for the bar chart.
product_names = [row[0] for row in revenue_rows]
revenues = [row[1] for row in revenue_rows]

# Prepare data for the line chart.
monthly_trend = {
    row[0]: row[1] for row in monthly_rows
}

# Generate both charts.
bar_chart_revenue_per_product(
    product_names,
    revenues
)

line_chart_monthly_trend(monthly_trend)

print("Both charts have been created successfully!")

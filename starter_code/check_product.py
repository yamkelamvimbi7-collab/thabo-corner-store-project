import sqlite3

conn = sqlite3.connect("store.db")

results = conn.execute(
    "SELECT product_id, product_name, unit_price "
    "FROM products WHERE product_name LIKE '%Coca-Cola%'"
).fetchall()

print("Coca-Cola product records:")
for row in results:
    print(row)

conn.close()

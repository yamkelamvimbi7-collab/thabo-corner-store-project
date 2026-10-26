
"""
data_cleaning.py
-----------------
Task 2: Load and clean the raw CSV files.
"""

import pandas as pd


def load_raw_data(products_path: str, sales_path: str):
    """Load both raw CSV files and return uncleaned DataFrames."""

    products_df = pd.read_csv(products_path)
    sales_df = pd.read_csv(sales_path)

    return products_df, sales_df


def clean_products(products_df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the products DataFrame."""

    # Work on a copy so the original data is not changed.
    products = products_df.copy()

    # Remove exact duplicate rows.
    products = products.drop_duplicates()

    # Remove products without a usable name.
    products["product_name"] = products["product_name"].replace(
        r"^\s*$", pd.NA, regex=True
    )
    products = products.dropna(subset=["product_name"])

    # Convert prices to numbers; invalid values become missing.
    products["unit_price"] = pd.to_numeric(
        products["unit_price"], errors="coerce"
    )

    # Remove products without a reliable price.
    # This avoids inventing prices for the sales analysis.
    products = products.dropna(subset=["unit_price"])

    # Standardise category names.
    products["category"] = (
        products["category"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    # Remove surrounding spaces from product names.
    products["product_name"] = products["product_name"].str.strip()

    # Reset row numbering after removing rows.
    products = products.reset_index(drop=True)

    return products


def clean_sales(
    sales_df: pd.DataFrame, valid_product_ids
) -> pd.DataFrame:
    """Return a cleaned copy of the sales DataFrame."""

    # Work on a copy.
    sales = sales_df.copy()

    # Remove exact duplicate rows.
    sales = sales.drop_duplicates()

    # Parse dates written in different formats.
    # format="mixed" requires pandas 2.0 or newer.
    sales["sale_date"] = pd.to_datetime(
        sales["sale_date"],
        format="mixed",
        errors="coerce"
    )

    # Remove missing or unparseable dates.
    sales = sales.dropna(subset=["sale_date"])

    # Store every date in YYYY-MM-DD format.
    sales["sale_date"] = sales["sale_date"].dt.strftime("%Y-%m-%d")

    # Convert quantities to numbers.
    sales["quantity"] = pd.to_numeric(
        sales["quantity"], errors="coerce"
    )

    # Remove rows without a usable quantity.
    sales = sales.dropna(subset=["quantity"])

    # Standardise product IDs to strings for comparison.
    sales["product_id"] = sales["product_id"].astype("string").str.strip()
    valid_ids = {str(product_id).strip() for product_id in valid_product_ids}

    # Remove missing and invalid product IDs.
    sales = sales.dropna(subset=["product_id"])
    sales = sales[sales["product_id"].isin(valid_ids)]

    # Use Unknown rather than guessing missing payment methods.
    sales["payment_method"] = (
        sales["payment_method"]
        .astype("string")
        .str.strip()
        .replace("", pd.NA)
        .fillna("Unknown")
    )
     # Handle missing customer types without deleting sales.
    sales["customer_type"] = (
    sales["customer_type"]
    .astype("string")
    .str.strip()
    .replace("", pd.NA)
    .fillna("Unknown")
)
    # Reset row numbering after cleaning.
    sales = sales.reset_index(drop=True)

    return sales


def cleaning_summary(
    raw_df: pd.DataFrame,
    clean_df: pd.DataFrame,
    name: str
) -> str:
    """Summarise how many rows were removed during cleaning."""

    raw_count = len(raw_df)
    clean_count = len(clean_df)
    removed_count = raw_count - clean_count

    return (
        f"{name}: {raw_count} raw rows -> "
        f"{clean_count} clean rows ({removed_count} removed)"
    )


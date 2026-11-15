import pandas as pd
from pathlib import Path
import sqlite3

root_dir = Path(__file__).resolve().parents[1]
data_path = root_dir / "data" / "sales_data.csv"
db_path = root_dir / "sales.db"


def load_data():
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} rows from {data_path}")
    return df


def clean_data(df):
    # Remove rows with missing critical values before string conversion
    df = df.dropna(subset=["order_id", "order_date", "region", "product", "quantity", "unit_price"])

    # Clean string columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

    # Convert data types
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    # Remove invalid rows after type conversion
    df = df.dropna(subset=["order_date", "quantity", "unit_price"])

    # Add revenue column
    df["revenue"] = df["quantity"] * df["unit_price"]

    # Standardize region/product names
    df["region"] = df["region"].str.title()
    df["product"] = df["product"].str.title()

    print(f"Cleaned data rows: {len(df)}")
    return df


def load_to_sqlite(df):
    conn = sqlite3.connect(db_path)
    df.to_sql("sales_data", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data loaded to SQLite database: {db_path}")


def main():
    df = load_data()
    df_cleaned = clean_data(df)
    load_to_sqlite(df_cleaned)

if __name__ == "__main__":
    main()

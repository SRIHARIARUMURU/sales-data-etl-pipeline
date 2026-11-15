import sqlite3
from pathlib import Path

import pandas as pd

root_dir = Path(__file__).resolve().parents[1]
data_path = root_dir / "data" / "sales_data.csv"
db_path = root_dir / "sales.db"


def load_data():
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} rows from {data_path}")
    return df


def clean_data(df):
    df = df.copy()

    string_columns = df.select_dtypes(include=["object", "string"]).columns
    for col in string_columns:
        df[col] = df[col].map(lambda value: value.strip() if isinstance(value, str) else value)

    critical_columns = [
        "order_id",
        "order_date",
        "region",
        "product",
        "quantity",
        "unit_price",
    ]
    df = df.dropna(subset=critical_columns)

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")

    df = df.dropna(subset=["order_date", "quantity", "unit_price"])

    df["revenue"] = df["quantity"] * df["unit_price"]

    for col in ["region", "product"]:
        if col in df.columns:
            df[col] = df[col].map(
                lambda value: value.strip().title() if isinstance(value, str) else value
            )

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

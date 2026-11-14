# Sales Data ETL Pipeline

A beginner-friendly ETL project built with Python and SQLite to clean sales data, transform it into a usable format, and analyze it using SQL.

## Project Goals
- Extract raw sales data
- Clean and transform it with Python
- Load it into a SQLite database
- Run SQL queries for business insights
- Document the workflow clearly for portfolio use

## Tech Stack
- Python
- Pandas
- SQLite
- SQL

## Dataset
The project generates a sample sales dataset with fields like:
- order_id
- order_date
- region
- product
- category
- customer_id
- quantity
- unit_price
- sales_channel

## Project Flow
1. Generate sample sales data
2. Read CSV with Python
3. Clean missing or inconsistent values
4. Add derived column: revenue
5. Load data into SQLite
6. Run SQL queries for analysis

## Folder Structure
```text
sales-data-etl-pipeline/
├── README.md
├── requirements.txt
├── data/
│   └── sales_data.csv
├── scripts/
│   ├── generate_sample_data.py
│   └── etl_pipeline.py
└── queries/
    └── sales_analysis.sql
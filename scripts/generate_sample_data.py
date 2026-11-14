import pandas as pd
from pathlib import Path

#create data directory if not exist
data_dir = Path(__file__).resolve().parents[1]/"data"
data_dir.mkdir(parents=True, exist_ok=True)

# Generate sample data
records = []

regions = ["North", "South", "East", "West"]
products = ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard"]
categories = ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"]
channels = ["Online", "Retail", "Wholesale"]


for i in range(1,501):
    region = regions [i % len(regions)]
    product = products [i % len(products)]
    category = categories [i % len(categories)]
    channel = channels [i % len(channels)]

    quantity = (i * 3) % 12 + 1
    unit_price = {
        "Laptop": 850,
        "Phone": 600,
        "Tablet": 420,
        "Monitor": 260,
        "Keyboard": 55
    }[product]

    revenue = quantity * unit_price

    records.append({
        "order_id": f"ORD-{i:04d}",
        "order_date": f"2024-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}",
        "region": region,
        "product": product,
        "category": category,
        "customer_id": f"CUST-{(i * 13) % 200 + 1:04d}",
        "quantity": quantity,
        "unit_price": unit_price,
        "revenue": revenue,
        "sales_channel": channel
    })

df = pd.DataFrame(records)
df.to_csv(data_dir / "sales_data.csv", index=False)

print("Sample sales data generated at:", data_dir / "sales_data.csv")
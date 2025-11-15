"""
ETL job to process pending payments and owed amounts.

This script:
- Merges sales_wholesale.csv with customers_wholesale.csv
- Filters unpaid invoices
- Aggregates outstanding amount and open invoice count per customer
"""

import warnings

from models import extract, transform, load

warnings.filterwarnings("ignore")

data = extract(
    sales_path="data/sales_wholesale.csv",
    customers_path="data/customers_wholesale.csv"
)

tdf = transform(data)
load(tdf)

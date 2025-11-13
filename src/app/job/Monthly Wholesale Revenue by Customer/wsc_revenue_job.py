"""
ETL script for the Monthly Wholesale Revenue by Customer job.

Extracts data from sales_wholesale.csv and customers_wholesale.csv applies transformations
such as data to compute total revenue, total boxes sold, and average price per box grouped
by month and customer loads the processed results into an output CSV file.
"""

import warnings

from models import extract, transform, load

# Ignore all warnings
warnings.filterwarnings("ignore")

# ETL pipeline
data = extract(
    sales_path="data/sales_wholesale.csv",
    customers_path="data/customers_wholesale.csv"
)

tdf = transform(data)
load(tdf)

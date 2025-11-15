"""
ETL script for the Under Transferred Boxes job.

This job extracts data from sales_wholesale.csv, applies transformations to
calculate monthly total ordered boxes, boxes sold, and under-transferred quantity
(i.e., boxes ordered but not sold). The transformed data is then exported to a CSV
file for reporting.
"""

from models import extract, transform, load


def main():
    """
    Run the Under Transferred Boxes ETL pipeline.

    - Extracts wholesale sales data from CSV.
    - Transforms the data to compute monthly ordered boxes, sold boxes,
      and under-transferred quantities.
    - Loads the final processed data into an output CSV.

    :return: None
    """
    data = extract(ws_path="data/sales_wholesale.csv", date_col="order_date")
    tdf = transform(data)
    load(tdf)

if __name__ == "__main__":
    main()
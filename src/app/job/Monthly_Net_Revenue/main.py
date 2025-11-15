"""
ETL script for the Monthly Net Revenue .

This job extracts data from sales_wholesale.csv and return_wholesale.csv, applies transformations to
calculate monthly total wholesale sales, return wholesale, and net revenue.
(i.e., To find total revenue per month). The transformed data is then exported to a CSV
file for reporting.
"""
import warnings

from models.extract import extract
from models.transform import transform
from models.load import load

"""
   Run the Monthly Net Revenue ETL pipeline.

   - Extracts wholesale sales data and Return wholesale from CSV.
   - Transforms the data to compute monthly wholesale sale, returns wholesale,
     and net revenue.
   - Loads the final processed data into an output CSV.

   :return: None
   """
# Ignore all warnings
warnings.filterwarnings("ignore")

data = extract(sw_path="C:/Users/Bk/PycharmProjects/etl-processing-engine-anwar-store/data/sales_wholesale.csv",
                   rw_path="C:/Users/Bk/PycharmProjects/etl-processing-engine-anwar-store/data/returns_wholesale.csv",
              )
tdf = transform(data)
load = load(tdf)
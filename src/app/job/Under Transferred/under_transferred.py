"""
    ETL to extract sales_wholesale.csv and group by month & product id,
    calculated total Total_ordered_boxes, boxes sold, and Needed_boxes per month and exported to csv file.
"""

import warnings

from models.extract import extract
from models.transform import transform
from models.load import load

# Ignore all warnings
warnings.filterwarnings("ignore")

data = extract(w_path="C:/Users/Bk/PycharmProjects/etl-processing-engine-anwar-store/data/sales_wholesale.csv",
                   #s_path="C:/Users/Bk/PycharmProjects/etl-processing-engine-anwar-store/data/stock_movement.csv",
              # p_path="C:/Users/Bk/PycharmProjects/etl-processing-engine-anwar-store/data/products.csv"
               )
tdf = transform(data)
load = load(tdf)
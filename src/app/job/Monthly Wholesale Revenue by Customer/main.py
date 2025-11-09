"""
    ETL to merge sales_wholesale.csv with customers_wholesale.csv and  group by month & customer,
    calculated total revenue, boxes sold, and avg price per box and exported to csv file.
"""
import warnings

from models.extract import extract
from models.transform import transform
from models.load import load

# Ignore all warnings
warnings.filterwarnings("ignore")

data = extract(s_path="C:/Users/anwar/PycharmProjects/etl-processing-engine-anwar-store/data/sales_wholesale.csv",
                   c_path="C:/Users/anwar/PycharmProjects/etl-processing-engine-anwar-store/data/customers_wholesale.csv")
tdf = transform(data)
load = load(tdf)
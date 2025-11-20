import warnings
from Modules.extract import extract
from Modules.transform import transform
from Modules.load import load

warnings.filterwarnings("ignore")

if __name__ == "__main__":

    sales_path = r"C:\Users\Nithya\PycharmProjects\etl-processing-engine-anwar-store\data\sales_retail.csv"
    products_path = r"C:\Users\Nithya\PycharmProjects\etl-processing-engine-anwar-store\data\products.csv"

    print("Extracting...")
    merged_data = extract(sales_path, products_path)

    print("Transforming...")
    transformed_data = transform(merged_data)

    print("Loading...")
    load(transformed_data)

    print("ETL Completed Successfully!")

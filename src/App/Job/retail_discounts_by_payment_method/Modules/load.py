import os
import pandas as pd

def load(data):
    """
    Save the transformed DataFrame to CSV.
    """

    output_path = r"src/App/Job/retail_discounts_by_payment_method/loaddata/retail_discounts_output.csv"

    # Create folder if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    data.to_csv(output_path, index=False)
    print("Data Loaded:", output_path)

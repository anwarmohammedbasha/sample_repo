"""
Extraction module for the Monthly Wholesale Revenue by Customer ETL job.

Reads sales and customer CSV data, parses dates, and merges both datasets on a common key column.
"""

import pandas as pd

def extract(sales_path, customers_path, key_col='customer_id', date_col='order_date'):
    """
        Extract and merge sales and customer data.

        Parameters
        ----------
        sales_path : str
            Path to the sales CSV file.
        customers_path : str
            Path to the customer CSV file.
        key_col : str, optional
            Column name to merge on (default is 'customer_id').
        date_col : str, optional
            Column in sales data to parse as date (default is 'order_date').

        Returns
        -------
        pandas.DataFrame
            Merged DataFrame containing sales and customer information.
    """

    # Read CSV files
    s_df = pd.read_csv(sales_path, parse_dates=[date_col], dayfirst=False, infer_datetime_format=True)
    c_df = pd.read_csv(customers_path, dayfirst=False, infer_datetime_format=True)

    # Merge data
    merged_df = s_df.merge(c_df, how='left', on=key_col)

    print("Data Extracted")
    return merged_df

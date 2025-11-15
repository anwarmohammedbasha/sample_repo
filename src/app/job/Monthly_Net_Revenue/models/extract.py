"""
Monthly Net Revenue  – Extract Module

This module reads the wholesale sales CSV and returns wholesale CSV files and loads it into a pandas
DataFrame for downstream processing. Date columns are parsed to ensure
correct datetime handling.
"""


import pandas as pd

def extract(sw_path, rw_path, key_col='invoice_id', date_col='order_date'):
    """
    Extract the sales and return data from the given CSV file.

    Parameters
    ----------
    sw_path : str
        Path to the wholesale sales CSV file.
    rw_path : str
        Path to the return wholesale CSV file.
    date_col : str
        Date columns to extract data from.

    Returns
    -------
    pandas.DataFrame
        Extracted sales data loaded into a DataFrame.
    """

    # Read CSV files
    sw_df = pd.read_csv(sw_path, parse_dates=[date_col], dayfirst=False, infer_datetime_format=True)
    rw_df = pd.read_csv(rw_path)

    # Merge data
    merged_df = sw_df.merge(rw_df, how='left', on=key_col)

    print("Data Extracted")
    return merged_df


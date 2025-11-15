"""
Under Transferred – Extract Module

This module reads the wholesale sales CSV file and loads it into a pandas
DataFrame for downstream processing. Date columns are parsed to ensure
correct datetime handling.
"""

import pandas as pd


def extract(ws_path, date_col='order_date'):
    """
    Extract the sales data from the given CSV file.

    Parameters
    ----------
    ws_path : str
        Path to the wholesale sales CSV file.
    date_col : str
        Date columns to extract data from.

    Returns
    -------
    pandas.DataFrame
        Extracted sales data loaded into a DataFrame.
    """
    w_df = pd.read_csv(
        ws_path,
        parse_dates=[date_col],
        dayfirst=False,
        infer_datetime_format=True,
    )

    print("Data Extracted")
    return w_df

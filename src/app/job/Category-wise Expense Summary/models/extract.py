"""
Category-wise Expense Summary – Extract Module

This module reads the raw expenses CSV file and loads it into a pandas
DataFrame for further transformation and summarization.
"""

import pandas as pd

def extract(expenses_path):
    """
    Extract the raw expenses data from a CSV file.

    :param expenses_path: Path to the expenses CSV file.
    :return: pandas DataFrame containing the raw expenses data.
    """
    df = pd.read_csv(expenses_path)
    print("Data Extracted")
    return df

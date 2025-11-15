"""
This module provides a function to efficiently read and combine
multiple CSV files from a specified directory into a single pandas DataFrame.
"""

import pandas as pd
import glob
import os

def extract(folder_path):
    """
    This function searches the specified directory for all files ending with
    the '.csv' extension, reads each one, and concatenates them vertically.

    Args:
        folder_path (str): The path to the folder containing the CSV files.

    Returns:
        pandas.DataFrame: A single DataFrame containing the data from all
                          read CSV files, concatenated sequentially.
    """
    search_pattern = os.path.join(folder_path, "*.csv")
    files = glob.glob(search_pattern)
    list_of_dfs = []
    for file in files:
        df = pd.read_csv(file)
        list_of_dfs.append(df)
    print(f'Successfully read: {len(list_of_dfs)}')
    combined_df = pd.concat(list_of_dfs)
    return combined_df

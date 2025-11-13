"""
Load module for the Category-wise Expense Summary ETL job.

This module handles the final load step of the ETL pipeline by writing the
processed and summarized expense data to a CSV file for reporting or downstream use.
"""

def load(df):
    """
    Load step for the Category-wise Expense Summary ETL job.

    Saves the transformed DataFrame to a CSV file.

    :param df: pandas DataFrame containing the summarized expenses.
    :return: None
    """
    df.to_csv("src/app/job/Category-wise Expense Summary/result/expense_summary.csv", index=False)
    print("Data Loaded")

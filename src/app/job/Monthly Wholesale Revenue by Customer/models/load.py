"""
Load module for the Monthly Wholesale Revenue by Customer ETL job.

This module handles saving the transformed DataFrame to a CSV file.
"""


def load(df):
    """
    Save the transformed DataFrame to a CSV file.

    :param df: pandas DataFrame containing the final transformed results.
    :return: None
    """
    df.to_csv(
        "src/app/job/Monthly Wholesale Revenue by Customer/result/ws_revenue_by_customer.csv",
        index=False
    )
    print("Data Loaded")

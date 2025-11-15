"""
Load module for the Under Transferred ETL job.

This module saves the final transformed DataFrame into a CSV file
inside the `result` directory for reporting and further analysis.
"""


def load(df):
    """
    Save the transformed DataFrame to a CSV file.

    :param df: pandas DataFrame containing the final transformed data.
    :return: None
    """
    df.to_csv(
        "src/app/job/Under Transferred/result/final.csv",
        index=False
    )
    print("Data Loaded")

"""
Load module for the Monthly Net Revenue ETL job.

This module saves the final transformed DataFrame into a CSV file
inside the `result` directory for reporting and further analysis.
"""


def load(df):
    """
       Save the transformed DataFrame to a CSV file.

       :param df: pandas DataFrame containing the final transformed data.
       :return: None
       """
    df.to_csv('C:/Users/Bk/PycharmProjects/etl-processing-engine-anwar-store/src/app/job/Monthly_Net_Revenue/loaddata/final.csv', index=False)
    print("Data Loaded")
"""
Load step of the ETL pipeline.

Saves the final transformed data into a CSV file.
"""


def load(data):
    """
    Save the transformed DataFrame as a CSV file.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame to save.

    Returns
    -------
    None
    """
    data.to_csv(
        'src/app/job/Pending Payments & Owed Amount/result/finaldata.csv',
        index=False
    )
    print('Data Loaded')

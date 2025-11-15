"""
Transformation module for the Category-wise Expense Summary ETL job.

This module prepares the expenses data for reporting by grouping
transactions by category and calculating total expenses for each
category.
"""

def transform(df):
    """
    Transform the raw expenses data by grouping it by category and
    calculating total expenses for each category.

    :param df: pandas DataFrame containing the raw expenses data.
    :return: pandas DataFrame with category-wise total expenses.
    """
    tdf = df.groupby("category").agg(total_expenses=('amount', 'sum')).reset_index()
    print("Data Transformed")
    return tdf

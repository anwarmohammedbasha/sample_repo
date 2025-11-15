"""
Data Transformation Module.

This module contains the 'transform' function calculates the total
expense per department, maps department IDs to meaningful names, and prepares
the data for loading.
"""

from datetime import date

def transform(data):
    """
        Aggregates expense data by department, maps department IDs to names,
        and adds a processing date.

        The input DataFrame is expected to have 'department_id' and 'amount' columns.

        Args:
            data (pd.DataFrame): The raw DataFrame containing daily expense records.
                                 Requires 'department_id' and 'amount' columns.

        Returns:
            pd.DataFrame: An aggregated DataFrame containing the 'department_name',
                          'total_expense', and 'ingest_date', sorted by total expense
                          in descending order.
    """
    agg_df = data.groupby('department_id').agg(total_expense=('amount', 'sum')).reset_index()
    department_map = {
        1: "HR",
        2: "Finance",
        3: "Operations",
        4: "Sales",
        5: "IT"
    }

    agg_df['ingest_date'] = date.today()
    agg_df['department_name'] = agg_df['department_id'].map(department_map)
    agg_df.drop('department_id', axis=1, inplace=True)
    agg_df.sort_values('total_expense', ascending=False, inplace=True)

    return agg_df
"""
Transformation module for the Monthly Net Revenue ETL job.

This module processes wholesale sales and return wholesale data to compute the
wholesale sale and return wholesale as per month, and identifies the
net sales of the month.
"""


def transform(df, date_col='order_date' , final_line_total_INR='final_line_total_INR', refund_amount_INR='refund_amount_INR'):
    """
        Transform the raw sales and return wholesale DataFrame to calculate Monthly Net Revenue.

        This function converts the date column to monthly periods, groups
        the data by month and calculates:
          - Total wholesale sales per month
          - Total return wholesale per month
          - Difference between Sales wholesale and return wholesale ("net_revenue")


        :param df: Input pandas DataFrame containing sales data.
        :param date_col: Name of the date column used for monthly grouping.
        :param final_line_total_INR: Column name for wholesale sales data.
        :param refund_amount_INR: Column name for return wholesale data.
        :return: Transformed pandas DataFrame with Monthly Net Revenue details.
        """

    df['month'] = df[date_col].dt.to_period('M').astype(str)
    tdf_df = df.groupby(['month']).agg(Total_wholesale_sales=(final_line_total_INR, sum),
                                                    Return_wholesale=(refund_amount_INR, sum),
                                                    ).reset_index()
    tdf_df['net_revenue'] = tdf_df['Total_wholesale_sales'] - tdf_df['Return_wholesale']
    print("Data Transformed")
    return tdf_df
"""
Transformation module for the Monthly Wholesale Revenue by Customer ETL job.

This module aggregates monthly total revenue, total boxes billed,
and computes the average price per box for each customer.
"""


def transform(df, date_col='order_date', revenue='final_line_total_INR', box='billed_quantity_boxes'):
    """
    Transform the raw sales DataFrame to produce monthly revenue metrics.

    This function converts the date column to monthly periods, groups
    the data by month and customer, and calculates:
      - Total revenue per customer per month
      - Total boxes billed per customer per month
      - Average price per box

    :param df: Input pandas DataFrame containing sales data.
    :param date_col: Name of the date column to convert and group by.
    :param revenue: Name of the revenue column used for summation.
    :param box: Name of the box quantity column used for summation.
    :return: Transformed pandas DataFrame with aggregated metrics.
    """
    df['month'] = df[date_col].dt.to_period('M').astype(str)

    tdf = df.groupby(['month', 'customer_id']).agg(
        total_revenue=(revenue, 'sum'),
        total_box=(box, 'sum')
    ).reset_index()

    tdf['total_revenue'] = round(tdf['total_revenue'], 2)

    tdf['avg_price_per_box'] = tdf.apply(
        lambda x: round((x['total_revenue'] / x['total_box']), 2),
        axis=1
    )

    print("Data Transformed")
    return tdf

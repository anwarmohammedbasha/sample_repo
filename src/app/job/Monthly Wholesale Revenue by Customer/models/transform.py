import pandas as pd

def transform(df, date_col='order_date', revenue='final_line_total_INR', box='billed_quantity_boxes'):
    """
        :param df: data frame
        :param date_col: date column to group
        :param revenue: revenue column
        :param box: box billed column
        :return: data frame
    """
    df['month'] = df[date_col].dt.to_period('M').astype(str)
    tdf_df = df.groupby(['month', 'customer_id']).agg(total_revenue=(revenue, 'sum'),
                                                               total_box=(box, sum)).reset_index()
    tdf_df['total_revenue'] = round(tdf_df['total_revenue'],2)
    tdf_df['avg_price_per_box'] = tdf_df.apply(lambda x: round((x['total_revenue']/x['total_box']),2), axis=1)
    print("======Data Transformed======")
    return tdf_df


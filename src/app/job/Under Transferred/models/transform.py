import pandas as pd

def transform(df, date_col='order_date' , order_quantity_boxes='order_quantity_boxes', billed_quantity_boxes='billed_quantity_boxes'):
    """
           :param df: data frame
           :param date_col: date column to group
           :param order_quantity_boxes: order_quantity_boxes column
           :param box: box billed column
           :return: data frame
       """
    df['month'] = df[date_col].dt.to_period('M').astype(str)
    tdf_df = df.groupby(['month', 'product_id']).agg(Total_ordered_boxes=(order_quantity_boxes, sum),
                                                    boxes_sold=(billed_quantity_boxes, sum),
                                                    ).reset_index()
    tdf_df['Needed_boxes'] = tdf_df['Total_ordered_boxes'] - tdf_df['boxes_sold']
    tdf_df = tdf_df[tdf_df['Needed_boxes'] > 0]
    print("======Data Transformed======")
    return tdf_df
"""
Transformation module for the Under-Transferred Boxes ETL job.

This module processes wholesale sales data to compute the number of 
boxes ordered vs boxes billed per product and month, and identifies 
cases where fewer boxes were transferred than ordered.
"""

def transform(
    df,
    date_col="order_date",
    order_quantity_boxes="order_quantity_boxes",
    billed_quantity_boxes="billed_quantity_boxes",
):
    """
    Transform the raw sales DataFrame to calculate under-transferred boxes.

    This function converts the date column to monthly periods, groups
    the data by month and product, and calculates:
      - Total ordered boxes per product per month
      - Total billed boxes per product per month
      - Difference between ordered and billed boxes ("Needed_boxes")
      - Products where billed quantity is less than ordered (under-transferred)

    :param df: Input pandas DataFrame containing sales data.
    :param date_col: Name of the date column used for monthly grouping.
    :param order_quantity_boxes: Column name for ordered box quantities.
    :param billed_quantity_boxes: Column name for billed box quantities.
    :return: Transformed pandas DataFrame with under-transferred box details.
    """

    df["month"] = df[date_col].dt.to_period("M").astype(str)

    tdf_df = (
        df.groupby(["month", "product_id"])
        .agg(
            Total_ordered_boxes=(order_quantity_boxes, "sum"),
            boxes_sold=(billed_quantity_boxes, "sum"),
        )
        .reset_index()
    )

    tdf_df["shortage_boxes"] = (
        tdf_df["Total_ordered_boxes"] - tdf_df["boxes_sold"]
    )

    tdf_df = tdf_df[tdf_df["shortage_boxes"] > 0]

    print("Data Transformed")
    return tdf_df

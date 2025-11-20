import pandas as pd

def extract(sales_path, products_path, key_col='product_id'):
    """
    Extract and merge sales and product data.
    """
    sales_df = pd.read_csv(sales_path)
    products_df = pd.read_csv(products_path)
    merged_df = pd.merge(sales_df, products_df, on=key_col, how='inner')
    return merged_df

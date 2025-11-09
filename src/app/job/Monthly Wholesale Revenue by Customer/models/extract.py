import pandas as pd

def extract(s_path,c_path, id_col='customer_id'):
    '''
    :param s_path: sales data path
    :param c_path: customer data path
    :return: merged  data
    '''
    s_df = pd.read_csv(s_path, parse_dates=['order_date'], dayfirst=False, infer_datetime_format=True)
    c_df = pd.read_csv(c_path, dayfirst=False, infer_datetime_format=True)
    merged_df = s_df.merge(c_df, how='left', on=id_col)
    print("======Data Extracted======")
    return merged_df

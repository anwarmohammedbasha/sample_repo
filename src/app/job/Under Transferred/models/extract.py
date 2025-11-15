import pandas as pd

#def extract(r_path,s_path,p_path, id_col='product_id'):
def extract(w_path):
    '''
      :param w_path: sales data path
      :return: Extracted sales data
      '''
    w_df = pd.read_csv(w_path, parse_dates=['order_date'], dayfirst=False, infer_datetime_format=True)
    #s_df = pd.read_csv(s_path)
    #p_df = pd.read_csv(p_path)

    #merged_df = r_df.merge(s_df, how='left', on=id_col)
    #merged_df = merged_df.merge(p_df, how='left', on=id_col)

    print("======Data Extracted======")
    return w_df


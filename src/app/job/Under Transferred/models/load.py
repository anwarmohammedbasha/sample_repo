import pandas as pd

def load(df):
    df.to_csv('C:/Users/Bk/PycharmProjects/etl-processing-engine-anwar-store/src/app/job/Under-Transferred_Retail_Days/loaddata/final.csv', index=False)
    print("======Data Loaded======")
import pandas as pd

def load(df):
    df.to_csv('C:/Users/anwar/PycharmProjects/etl-processing-engine-anwar-store/src/app/job/Monthly Wholesale Revenue by Customer/loaddata/final.csv', index=False)
    print("======Data Loaded======")
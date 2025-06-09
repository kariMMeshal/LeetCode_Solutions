import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged= pd.merge(company,orders,on='com_id',how='inner')
    merged=merged[merged['name']=='RED']
    rslt = sales_person[~sales_person['sales_id'].isin(merged['sales_id'])]

    return(rslt[['name']])
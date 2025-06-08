import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    rslt = activities.groupby('sell_date')['product'].nunique().reset_index().rename(columns={'product': 'num_sold'})
    rslt['products'] = activities.groupby('sell_date')['product'].apply(list).reset_index() [['product']]
    rslt['products'] =  rslt['products'].apply(lambda x: ','.join(sorted(set(x))))
    rslt.sort_values(by='sell_date' , inplace=True)
    return(rslt)
import pandas as pd 

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    count = employee.groupby('managerId').size().reset_index().rename(columns={'managerId':'id',0:'count'})
    count=count[count['count']>=5]
    count= count[ count['id'].isin(employee['id']) ]
    rslt = pd.merge(employee,count,on='id',how='right')
    return(rslt[['name']])   
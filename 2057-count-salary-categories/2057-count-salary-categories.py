import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts['income'] < 20000].count()['income']
    avg = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].count()['income']
    high = accounts[accounts['income'] > 50000].count()['income']
    

    rslt = pd.DataFrame({
        'category':['Low Salary' , 'Average Salary' , 'High Salary'],
        'accounts_count':[low , avg , high]
        })
      

    return(rslt)
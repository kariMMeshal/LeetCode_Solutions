import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(inplace=True , subset='salary')
    employee.sort_values(inplace=True , by='salary' , ascending=False)
    employee.reset_index(drop=True , inplace=True)
    rslt = pd.DataFrame([{f'getNthHighestSalary({N})' : None}]  )
    if(len(employee) <  N or N <= 0):return rslt
    else:
        rslt[f'getNthHighestSalary({N})'][0] = employee['salary'][N-1]
        return rslt

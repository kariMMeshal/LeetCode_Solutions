import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.drop_duplicates(inplace=True , subset='salary')
    employee.sort_values(inplace=True , by='salary' , ascending=False)
    employee.reset_index(drop=True , inplace=True)
    rslt = pd.DataFrame([{'SecondHighestSalary' : None}]  )
    if(len(employee) <  2 ):
        return rslt
    else:
        rslt['SecondHighestSalary'][0] = employee['salary'][1]    
        return rslt
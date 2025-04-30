import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    merged = employee.merge(department,left_on='departmentId' , right_on='id')
    highest_salary = merged.groupby('departmentId').apply(lambda x: x[ x['salary']==x['salary'].max() ] )
    highest_salary.rename(columns={'name_x':'Employee' , 'salary':'Salary' , 'name_y' :'Department'} ,inplace=True )
    return highest_salary[['Employee','Salary','Department']]
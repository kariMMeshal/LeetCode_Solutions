import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = 0
    employees.loc[(employees['employee_id'] % 2 != 0) & (employees['name'].str[0] != 'M'), 'bonus'] += employees['salary']
    employees.sort_values(by=['employee_id'] , inplace=True)
    print(employees[['employee_id','bonus']])   
    return employees[['employee_id','bonus']]
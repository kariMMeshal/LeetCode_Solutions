import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return  patients[patients['conditions'].str.match('^[a-zA-Z0-9\s]*(\s|^)DIAB1[\sa-zA-Z0-9]*') ] 
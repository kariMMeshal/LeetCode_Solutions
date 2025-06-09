import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(students, subjects, how='cross').sort_values(by='student_id')
    pairs = examinations.groupby(['subject_name','student_id']).size().reset_index()
    rslt= pd.merge(merged,pairs,on=['student_id', 'subject_name'],how='left').rename(columns={0:'attended_exams'}).sort_values(by=['student_id', 'subject_name'])
    rslt['attended_exams'] = rslt['attended_exams'].fillna(0)

    return(rslt)
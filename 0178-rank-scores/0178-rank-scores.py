import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(axis = 0,method = 'dense', ascending = False)
    scores.sort_values('rank', ascending = True, inplace = True)
    return(scores[['score' , 'rank']])
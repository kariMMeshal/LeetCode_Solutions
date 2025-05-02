import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
# Use .rank() assigns ranks to scores:
# - axis=0: apply method on columns
# - method='dense': same values get the same rank, next rank is consecutive
# - ascending=False: higher scores get lower rank numbers (1 is highest)
    scores['rank'] = scores['score'].rank(axis = 0,method = 'dense', ascending = False)
    scores.sort_values('rank', ascending = True, inplace = True)
    return(scores[['score' , 'rank']])

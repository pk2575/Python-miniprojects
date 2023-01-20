 # Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three
 # occurrences of five. Return True otherwise False.

import pandas as pd

def has_values(list):
    df = pd.Series(list)
    df = df.groupby(df).size()
    try:
        if (df[19] == 2) and (df[5] >= 3):
            return True
        else: 
            return False
    except KeyError:
        return False
list = [19, 19, 5, 5, 5, 5, 5]
print(has_values(list))
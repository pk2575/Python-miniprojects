# url: https://www.w3resource.com/python-exercises/puzzles/index.php


# TASK: 1
 # Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three
 # occurrences of five. Return True otherwise False.


import pandas as pd

def task1(list):
    df = pd.Series(list)
    df = df.groupby(df).size()
    try:
        if (df[19] == 2) and (df[5] >= 3):
            return True
        else: 
            return False
    except KeyError:
        return False

# TASK: 2
#  Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true
#  if the length of the list is 8 and the fifth element occurs thrice in the said list.

def task2(list):
    return (len(list) == 8) and (list.count(list[4]) == 3)

# TASK: 3
# Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34

def task3(num):
    return (num > 4**4) and (num % 34 == 4)

# TASK: 4

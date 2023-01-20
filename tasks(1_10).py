# url: https://www.w3resource.com/python-exercises/puzzles/index.php


# TASK: 1
 # Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three
 # occurrences of five. Return True otherwise False.

def task1(list):
    import pandas as pd
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
# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as
# possible. Write a Python program to find the number of stones in each pile.
def task4(n):
    return list(range(n,(n + 2 * n),2))

# TASK: 5
#Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
def task5(str_list):
    return (str_list[-2] in str_list[-1])

# TASK: 6
# Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one 
# another. Return True otherwise False.
def task6(num_list):
    import numpy as np
    array = np.array(num_list)
    diff_list =  np.diff(num_list)
    return np.all(diff_list == 10)


# TASK: 7

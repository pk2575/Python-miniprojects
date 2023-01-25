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
# Write a Python program to check a given list of integers where the sum of the first i integers is i.

def task7(list):
    import numpy as np
    ary = np.array(list)
    for x in range(len(list)):
        print(x)
        print(np.sum(ary[:(x)]))
        while x != np.sum(ary[:(x)]):
            return False
    return True

#TASK: 8
# Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.
def task8(string):
    import re
    merged = re.split(r"([ ,]+)",string)
    return merged[::2], merged[1::2]

#TASK: 9
#Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats
#twice consecutively among the first twenty entries.
def task9(lst):
    return (len(set(lst)) == 4) and all(x != lst[idx-1]   for x, idx in enumerate(lst))

#TASK: 10
#Given a string consisting of whitespace and groups of matched parentheses, write a Python program to split it into
#groups of perfectly matched parentheses without any whitespace.
def task10(string):
    filtered =[]
    s0 = string.replace(" ", "")
    s1 = ""
    for x in s0:
        s1 += x
        if s1. count("(") == s1.count(")") :
            filtered.append(s1)
            s1 = ""
    return filtered

#Task 11:
# Write a Python program to find the indexes of numbers in a given list below a given threshold
def task11(list, threshold):
    valid_indices = []
    for indx, entry  in enumerate(list):
        print(entry, indx)
        if entry < threshold:
            valid_indices.append(indx)
    return (valid_indices)



#Task 12
#Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
def task12(string_list):
    is_pallindrome = []
    for string in string_list:
        is_pallindrome.append( string == string[::-1])
    return is_pallindrome

#Task 13
# Write a Python program to find strings in a given list starting with a given prefix
def task13(str_list, prefix):
    return [x for x in str_list if x.startswith(prefix)]

#Task 14
#Write a Python program to find the length of a given list of non-empty strings
def task14(str_list):
    return [len(x) for x in str_list]

#Task 15
# Write a Python program to find the longest string in a given list of strings.
def task15(str_list):
    return(max(str_list, key= len))


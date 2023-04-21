# TASK 31
# Write a Python program to find the coordinates of a triangle with given side lengths
# beyond python

# TASK 32
# Write a Python program to rescale and shift numbers in a given list, so that they cover the range [0, 1].
def task32(lst):
    maxm = max(lst)
    minm = min(lst)
    return [(num - minm)/(maxm - minm) for num in lst] 

# TASK 33
# Write a Python program to find the positions of all uppercase vowels (not counting Y)
# in even indices of a given string.

def task33(string):
    return [ indx for indx in range(0,len(string),2) if string[indx] in [ "A", "E", "I", "O", "U"]]

# TASK 34
#  Write a Python program to find the sum of the numbers in a given list among the first k with more than 2 digits.
def task34(lst, k):
    return sum( [num for num in lst[:k] if len(str(num)) > 2] )

# TASK 35
# Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
def task35(num):
    import numpy as np
    num = str(num)
    nums = [ int(digit) for digit in num if int(digit)%2 == 1]
    if len(nums) > 0:
        return np.prod(nums)
    return 0

# TASK 36
# Write a Python program to find the largest k numbers from a given list of numbers.
def task36(lst, k):
    import numpy as np
    lst = np.sort(lst)
    return lst[-k:]

# TASK 37

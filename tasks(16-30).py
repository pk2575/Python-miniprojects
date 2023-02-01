#TASK 16
# Write a Python program to find strings in a given list containing a given substring.

def task16(sub_str,list):
    return [x for x in list if sub_str in x]

# TASK 17
# Write a Python program to create a string consisting of non-negative integers up to n inclusive
def task17(count):
    return " ".join(map (str,range(count+1)))

# TASK 18
# An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row.
# Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them,
# but they are useful as arrays in computing. Write a Python program to find the indices of all occurrences of target in
# the uneven matrix.
def task18(matrix,target):
    return [[i,j]for (i, values) in enumerate(matrix) for (j, x) in enumerate(values) if x == target]


# TASK 19
# Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if
# there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).
def task19(string):
    if ("," in string) or (" " in string) :
        import re
        pattern = re.compile(r"[, ]")
        return re.split(pattern,string)
    else:
        return [letter for letter in string if string.islower() and ord(letter)%2 == 0]


# TASK 20
# Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
def task20(lst):
    if all( lst[i] < lst[i + 1] for i in range(len(lst)-1)):
        return str("Increasing")
    elif all( lst[i] > lst[i + 1] for i in range(len(lst)-1)):
        return str("Decreasing")
    else:
        return str("Not a monotonic sequence!")


# TASK 21
# Write a Python program to check, for each string in a given list,
# whether the last character is an isolated letter or not. Return True otherwise False. 
def task21(lst):
    return [len(word.split(" ")[-1]) == 1 for word in lst]


# TASK 22
# Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.
def task22(str):
    return sum(ord(char) for char in str if char.isupper())


# TASK 23
# Write a Python program to find the indices at which the numbers in the list drop.
def task23(lst):
    return [ (idx + 1) for idx in range(len(lst)-1) if lst[idx] > lst[idx +1]]

# TASK 24
# Write a Python program to create a list whose ith element is the maximum of the first i elements from an input list.
def task24(lst):
    return [max(lst[ :i]) for i in range(1, len(lst) + 1 )]

# TASK 25/26
# Write a Python program to find the largest number where commas or periods are decimal points.
def task26(lst):
    return max(lst, key = lambda x : float(x.replace(",","."))).replace(",", ".")

# TASK 27
# Write a Python program to find x that minimizes the mean squared deviation from a given list of numbers.
def task27(lst):
    return sum(lst)/len(lst)

# TASK 28
# Write a Python program to select a string from a given list of strings with the most unique characters.
def task28(lst):
    return max(lst, key= lambda x : len(set(x)))

# TASK 29
# Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
def task29(lst):
    for i in lst:
        if i > 0:
            if -i in lst:
                return [lst.index(i), lst.index(-i)]

# TASK 30
# Write a Python program to find a list of strings that have fewer total characters (including repetitions).
def task30(lst):
    sums = [sum(len(word) for word in group) for group in lst]
    return lst[sums.index(min(sums))]
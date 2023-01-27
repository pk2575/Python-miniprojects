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

        
#  Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true
#  if the length of the list is 8 and the fifth element occurs thrice in the said list.

def is_valid(list):
    return (len(list) == 8) and (list.count(list[4]) == 3)

list = [19, 15, 11, 7, 5, 6, 2]
print(is_valid(list))
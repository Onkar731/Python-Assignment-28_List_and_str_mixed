"""
Write a python script to remove all non int values from a list
"""

# defining a list of different types of values
l1 = [23, 45.8, 'Onkar', True, 4+5j, False, 345, 100, 23.5, 456, 475.222, 890, True]

# removing non int values from the list
i = 0
while i < len(l1) :
    if type(l1[i]) != int :
        l1.remove(l1[i])
        i -= 1
    i += 1

# printing list of remaining values
print("List after removing non int values :", l1)
"""
Write a python script to print distinct elements along with their frequencies of
occurrences in the list
"""

# defining a list of duplicate elements
l1 = [1,2,3,4,5,6,6,1,2,4,4,3,0,9,8,7,6,0,0,9,8,8,7,7,6,6,1,2,3,4,6,6,7,8,9,]

# also creating a empty list
l2 = list()

# printing distinct elements along with their frequencies
for e in l1 :
    if e not in l2 :
        print(e, "-->", l1.count(e))
        l2.append(e)

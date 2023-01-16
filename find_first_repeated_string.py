"""
Write a python script to find first repeated string in a list of strings
"""

# defining a list of strings
l1 = ['mysirg', 'onkar', 'education', 'yogesh', 'services', 'nikhil', 'raj', 'onkar', 'raj', 'onkar', 'nikhil', 'onkar']


# finding first repeated string in a list of strings
for string in l1 :
    if l1.count(string) > 1 :
        print("First repeated string is \'%s\'" %(string))
        break;

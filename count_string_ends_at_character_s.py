"""
Write a python script to count strings which ends at chacracter 's'
in a list of strings
"""

# defining a list of strings
l1 = ['trees', 'onkar', 'ends', 'yes', 'services', 'nikhil', 'raj', 'onkar', 'sis', 'onkar', 'nikhil', 'strings']

# counting strings which ends at character 's'
count = 0

for string in l1 :
    if string.endswith("s") :
        count += 1
    
# printing count of strings which ends at character 's'
print("Number of strings ends at character 's' :", count)
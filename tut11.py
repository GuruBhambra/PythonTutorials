# Sets in Python

"""
Sets are unordered, immutable and do not allow duplicate values
methods like union and intersection are there n the sets
"""

s = set()
# print(type(s))

s1 = {1,2,3,4,4,4,4,5}
f1 = {"fruits", "apple", "mango", "grapes", "watermelon", "pineapple", "orange"}


s2 = {6,7,8,9}
s3 = s1.union(s2)
s4 = s1.difference_update(s2)
s5 = s1.isdisjoint(s2)
print(f1)
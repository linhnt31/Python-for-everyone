""" Operations on sets

"""
a = {1, 2, 3, 'linh'}
b = {2, 3, 'minhnt'}

# intersection
print(a.intersection(b))
print(a & b)
print(a, " ", b)

# Union(): returns a set that contains all items from the original set, and all items from the specified sets.
c = {'1', '2', 3}
d = {1, 2, 3}
print(c.union(d))
print(c | d)

# Difference 
print(c.difference(d))
print(c - d)

# add and remove
"""
- discard(): If the element is not present in the set, then no error or exception is raised 
- remove():  the element is not present in the set, then error or exception is raised 
""" 
c.add(102.5)
print(c)
c.discard('1') 
print(c)


""" Get the unique elements of a list
"""

a = [1, 2, 3, 1, 2, "linhnt", 'linhnt']
print(list(set(a)))

""" Set of sets
"""
#b = {{1, 2}, {3, 4}} # Error
b = {frozenset({1, 2}), frozenset({3, 4})}
print(b)
print(len(b))

"""Multisets
- Counter(): 
    + is a dictionary 
    + unordered collection
"""
from collections import Counter
listA = ['a', 'b', 'b', 'c']
counterA = Counter(listA)
print(counterA, type(counterA))
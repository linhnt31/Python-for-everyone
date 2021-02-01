"""Set
- unordered collections (<==> dictionary) of unique objects
- 2 types: 
+ Mutable and new elements can be added
+ Frozen Sets
"""

# Type 1
fruits = {'apple', 'orange', 'banana', 'banana'} # duplicates will be removed.
print(fruits, type(fruits))
a = set('linhnt')
a.add('hp')
print(a)

# Type 2: immutable and new elements cannot be added
b = frozenset('acnjasnc')
print(b)
#print(type(b))


"""List 
- like arrays but it can have different data types
"""
l = [123, 'abc', 10.2, 'linhnt']
print(l)
print(l*2)


"""Dictionary
- {key:value} pairs
"""
dic = {'linh': 19, 'minh':20}
dic['minh'] = 22
print(dic)
print(dic.values()) # return a list of values
print(dic.keys()) # return a list of keys


"""Tuple
- ()
- immutable
"""
tup = (123, 'linhnt', ['a', 'b'])
print(tup)
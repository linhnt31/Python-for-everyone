"""
- List is mutable
"""

a = []

a.append('hello')
a.append(10)
b = [8, 9, 10, 4]
c = [11, 12, 13]
a.extend(b)

a += c

a.reverse()
b.sort()

print(a)
print('b: ', b)
print('Index of 10 is: ', a.index(10))
print(a.count(10))

a.clear()

""" Better way to sort using "attrgetter" (for attributes of object) and "itemgetter"
- "key=" can be used with max, min and sorted

"""
from operator import attrgetter, itemgetter

people = [{'name':'chandan','age':20,'salary':2000},
            {'name':'chetan','age':18,'salary':5000},
            {'name':'guru','age':30,'salary':3000}]

by_age = itemgetter('age')

people.sort(key=by_age)

max_age = max(people, key=by_age)
print(people)
print(max_age)


a = list(range(10))
b = a # a and b point to the same memory.
b[0] = 10
copy_lst = a[:]
print(copy_lst)
copy_lst[0] = 100
print(a)

"""
- To check a element whether it exists in list --> using "in" keyword and convert "list" into "set" to boost speed.
"""

""" any & all
- *all*: is to determine if all the values in an iterable --> True
- *any*: is to determine if one or more values in an iterable --> True
"""

nums = [1, 0, 1, 1]
chars = ['a', 'b', 'c', None]
print(all(nums))
print(all(chars))
print(any(nums))

vals = [1, 2, 3, 4]
print([val > 12 for val in vals])
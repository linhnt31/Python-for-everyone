a = range(10)
odd_nums = [x for x in a if x & 1]

print(odd_nums)

non_vowels = [x if x in 'ueoai' else '*' for x in 'apple']
print(non_vowels)

sorted_lst = [sorted(x) for x in [[2, 1], [4, 3], [0, 1]]]
print(sorted_lst)

"""
- randint(): random integer in range [a, b], including both end points.
- randrange(): does not include the end points.
"""

from random import randint, randrange

lst1 = [randrange(1, 10) for _ in range(20)]
lst2 = [randint(1, 10) for _ in range(20)]
print(lst1)
print(lst2)

""" List comprehensions with nested loops
"""

data = [[1, 2], [3, 4], [5, 6]]
output = [x for d in data for x in d]
print(output)
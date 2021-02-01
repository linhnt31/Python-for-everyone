# {key: value} - Mapping
# a dict is unsorted and keys are unique

d1 = {'linh' :'nt'}
d2 = dict(minh=[1, 2, 3])

d3 = {'linh':99}
print(d3, d2, d1)

"""
- Access a non-existent key --> "KeyError" exception

--> Solution: 
1. Using "dict.get(key, default_value)"

+ It does not add "key" to my dict
+ If key exists --> return value
+ Else, return default value

2. Catching "exception"
"""

myDict = {'linhnt' : 2000}
#print(myDict['abc']) --> KeyError
print(myDict.get('linhnt', 1999))

# key = input('Enter a key: ')
# value = input('Enter a value respectively: ')
default_value = None

# try:
#     value = myDict[key]
# except KeyError:
#     value = default_value

""" Iterating over a dictionary

"""
d = {'a': 1, 'b': 2, 'c':3}
for key in d: 
    print(key, d[key])

print([key for key in d])

for key, value in d.items():
    print(key, value)

for value in d.values():
    print(value)

""" Dictionary with default values

- "dict.setdefault" : create a new instance of the initial value if the key did not exist before.
"""

from collections import defaultdict

d = defaultdict(int)
d['key']
d['key1']
print(d, type(d))


d1 = {}
d1.setdefault('Another_key', []).append('This worked')
print(type(d1))
print(d1)


""" Accessing keys and values
"""

myDict = {
    'a' : 1,
    'b' : 2
}

print(myDict.keys()) # return a list of key
print(myDict.values())
tmp = list(myDict.items())
tmp.sort()
print(tmp)
print(tmp[0], type(tmp[0])) # ('a', 1) <class 'tuple'>


""" Creating an ordered dictionary
- Using "OrderedDict" --> return dictionary elements in the original insertion order.
"""
from collections import OrderedDict

d = OrderedDict()
d['first'] = 1
d['zero'] = 0 
d['a'] = 10

print(dict(d)) # {'first': 1, 'zero': 0, 'a': 10}


""" All combinations of dictionary values
"""
import itertools

options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]
}

keys = list(options.keys())
values = [options[key] for key in keys]

print(keys)
print(values)

combinations = [dict(zip(keys, combination)) for combination in itertools.product(*values)]
print(combinations)



""" Sort a dictionary by values
"""

d = {'a' : 2, 'd' : 1, 'c' : 10, 'b' : 3}
sorted_dict = {k: v for k, v in sorted(d.items(), key= lambda item: item[1], reverse=True)}
print(sorted_dict)
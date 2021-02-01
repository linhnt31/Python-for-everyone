""" Dictionary comprehension 
- is similar to a list comprehension
- output: produces a dictionary obj
"""

d = {x : x*x for x in (1, 2, 3, 4)}
print(d)

names = {name: len(name) for name in ('linhnt', 'minhh', 'anduong') if len(name) > 5}
print(names)

# Swapping keys and values

swapped = {v: k for k, v in names.items()}
print(swapped)

# Merging dictionaries
dict1 = {'a' : 1, 'b': 2}
dict2 = {'c' : 3, 'd': 4}

merged_dict = {k: v for d in [dict1, dict2] for k, v in d.items()}
print(merged_dict)
# Ref: https://www.geeksforgeeks.org/defaultdict-in-python/

""" Syntax: defaultdict(default_factory)
+ default_factory: It is a function returning the default value for the dictionary defined. If this argument is absent then the dictionary raises a KeyError.

- *defaultdict* never raises  a **KeyError**.
    + Because it provide *a default value* for the *key* that does not exist before.
"""

from collections import defaultdict

d = defaultdict(lambda: "Not present")
d['a'] = 1
d['b'] = 2

print(d['a'])  # 1
print(d['c'])  # Not present

### When the list class is passed as the default_factory argument,
#  then a defaultdict is created with the values that are list.
d1 = defaultdict(list)
for i in range(5):
    # d1[i] = i # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
    d1[i].append(i)

print(d1)

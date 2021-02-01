# Ref: https://www.guru99.com/python-counter-collections-example.html

""" Find the key with the largest value by using Counter
- Ref: https://www.robjwells.com/2015/08/python-counter-gotcha-with-max/
"""


""" Python Counter
- data is held in an *unordered collection* (keys) - *ordered* (values) (descending)
- is used for iterable objects
- Holding the count of each of the elements present in the container.
- is a subclass inside **the dictionary class**
    + Using Python Counter can count the *key-value* pairs in an obj(hash table obj)
"""
from collections import Counter

### Counter with String
my_str = "linhnt research student"
print(Counter(my_str), type(Counter(my_str)))
# Output: Counter({'n': 3, 't': 3, 'e': 3, 'h': 2, ' ': 2, 'r': 2, 's': 2, 'l': 1, 'i': 1, 'a': 1, 'c': 1, 'u': 1, 'd': 1}) <class 'collections.Counter'>

### Counter with list
list1 = ['x','y','z','x','x','x','y','z']
print(Counter(list1))
# Output: Counter({'x': 4, 'y': 2, 'z': 2})

### Counter with dictionary ---> I do not understand how Counter counts 'z' here ???
dict1 =  {'x': 4, 'y': 2, 'z': 10, 'z': 3, 'z': 4}
print(Counter(dict1))
# Output: Counter({'x': 4, 'z': 4, 'y': 2})

""" Operations with Counter
"""

# Initializing
_count = Counter()

# Adding values to the Counter
_count.update('Hello linhnt')
print(_count)

# Accessing the Counter
for char in _count:
    print('{} : {}'.format(char, _count[char]))

# Deleting an element from Counter
# Using *del* keyword
del _count['H']
print(_count)

# most_common(n) - return a list of tuple +  n: lists the number of most common elements
encryptedText = '$~NmiNmim$/NVeirp@dlzrCCCCfFfQQQ'
print(Counter(encryptedText).most_common(2)[0][0]) # key
print(Counter(encryptedText).most_common(2)[0][1]) # value
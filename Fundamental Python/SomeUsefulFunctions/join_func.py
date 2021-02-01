""" string_name.join(iterable) - iterable: list, tuple, string, set, dict
- is a string method and return a string
"""

# Problem: https://app.codesignal.com/arcade/python-arcade/caravan-of-collections/zmQ9DqAN2mDL9hive/solutionshttps://app.codesignal.com/arcade/python-arcade/caravan-of-collections/zmQ9DqAN2mDL9hive/solutions

word = {'a', 'b', 'c'}

joined_str = '-'.join(sorted(word))
print(joined_str) # a-b-c
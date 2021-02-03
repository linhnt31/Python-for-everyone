# Ref: https://github.com/linhnt31/30-Days-Of-Python/blob/master/13_Day_List_comprehension/13_list_comprehension.md

""" Lambda Function
- without a name, can only have one expression
- Usage: write an anonymous func inside another func
    + Best use case of "lambda" is in function like "map", "filter", "reduce"

- EXERCISES: 
    + ./CodeSignal/twinsScore.py
"""

# Creating a lambda function
func = lambda p1, p2: p1 + p2 

#print(type(func))
#print(func(4, 5)) # 9

# Lambda function inside another function
def power(x):
    return lambda n: x ** n 

cube = power(2)(3)
#print(cube) # 8

""" map(func, iterable) """

numbers = range(5)

def square(x):
    return x ** 2

# squared_numbers = list(map(square, numbers))
squared_numbers = list(map(lambda x: x ** 2, numbers))
#print(squared_numbers) # [0, 1, 4, 9, 16]

numbers_str = ['1', '2', '3']
numbers_int = list(map(int, numbers_str))
#print(numbers_int) # [1, 2, 3]


names = ['linh', 'minh', 'hai']
def change_to_upper(name):
    return name.upper()

# names_upper_cased = list(map(change_to_upper, names))
names_upper_cased = list(map(lambda name: name.upper(), names))
#print(names_upper_cased) # ['LINH', 'MINH', 'HAI']

# Combine 2 lists
b = [22, 13, 45, 32]
m = [28, 41, 13, 32]

ans = list(map(lambda x, y: x + y, b, m))
print(ans)


""" filter(func, iterable)

- returns boolean for each item of specified iterable.
- It filters the items that satify the filtering criteria.
""" 

numbers = range(5)

def is_even(num):
    if num & 1 == 0:
        return True
    return False

# even_numbers = list(filter(is_even, numbers))
even_numbers = list(filter(lambda x : x & 1 == 0, numbers))
#print(even_numbers)

""" reduce(func, iterable)
- from functools import reduce
- Combine 2 elements 
"""
from functools import reduce
numbers_str = ['1', '2', '3']
def add_two_numbers(x, y):
    return int(x) + int(y)

total = reduce(add_two_numbers, numbers_str)
#print(total)

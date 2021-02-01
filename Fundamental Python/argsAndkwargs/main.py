# Ref: https://viblo.asia/p/python-args-va-kwargs-gDVK2pdnlLj

""" *args 
- is a *tuple* #1
- Using for the rest of elements #2
"""

#1 Using when we dont know exactly how many arguments needed to be input
def foo(*args):
    res = 0
    for v in args:
        res += v
    print(res)

foo(1, 2)
foo(1, 2, 3, 4)

#2 When we dont know a few first elements - *args: the rest
def foo2(a, b, *args):
    print(type(args))
    print('Known elements: ', a, b)
    for v in args:
        print('Rest: ', v)

foo2(1, 2, 3, 4, 10, 22)

""" **kwargs
- is a dict{key:value...}
    + when passing arguments to functions - *keys* must have *default values*.
- Using for **named arguments** or **keyword arguments**.
"""

def foo3(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

foo3(a=1, b=2, c=10)


""" Unpack
- "*" is used for **iterable**
- "**" is only used for "dict".
"""
x = [1, 2, 3]
y = (1, 2, 3, 4)
z = {'a': '1', 'b': '2', 'c': '3'}

def foo4(a, b, c):
    print('a = {} -b = {} -c = {}'.format(a, b, c))
print(*x)
print(*y)
foo4(**z)

# Unpack when assigning variables
a  = range(6) # a = [0, 1, 2, 3, 4, 5]

b, *c, d = a # b = 0, c = [1, 2, 3, 4], d = 5

print(b, c, d)

# 

dict1 = {"A": 1, "B": 2}
dict2 = {"C": 3, "D": 4}
dict3 = {**dict1, **dict2}
print(dict3)

m = [*x, *y]
print(m)
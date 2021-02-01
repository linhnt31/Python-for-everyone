"""
- *Decorators* are software **design patterns**.
- Functions: 
    + Altering the functionality of a function, method or class *without* use directly **subclasses** or change source code. 
"""

""" Decorator func
- We always define *a new function* inside decorator and return it
- How it works: #2
    + The decorator would first do something that it needs to do
    + Then, call the original func
    + Finally, process the return value
"""
def super_secret_func(f):
    return f

@super_secret_func
# <===> my_func = super_secret_func(my_func)
def my_func():
    print('This is my favorite function')

my_func()

#2
"""This is the decorator"""
def print_args(func):
    def inner_func(*args, **kwargs):
        print(args)
        print(kwargs)
        return func(*args, **kwargs)
    return inner_func

@print_args
def multiply(a, b):
    print('A new func')
    return a+b

print(multiply(3, 5)) 
# (3, 5)
# {}
# A new func
# 8
print('-'*20)


""" Decorator Class
- *my_func* gets replaced with an instance of the *decorator* class.
- Decorating methods
    + We need to define *__get__* method
"""
from types import MethodType

class Decorator(object):
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print('Before the function called')
        res = self.func(*args, **kwargs)
        print('After the function called')
        return res
    def __get__(self, instance, cls):
        # Return a method if it is called on an instance
        return self if instance is None else MethodType(self, instance)

class Test(object):
    @Decorator
    def __init__(self):
        pass

@Decorator
def testFunc():
    print('Inside the function')

obj1 = Test()

#testFunc()
# Before the function called
# Inside the function
# After the function called
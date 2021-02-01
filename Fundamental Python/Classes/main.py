"""
- A class is made up of *attributes(data)* and *methods(functions)*
- A Object is an instance of a class
- By default, elements imitates the behaviors of the C++/Java *public* keyword

- __functionName__(self, other_stuff) : *magic methods* 
    + *Overloading* is implemented with *magic methods*
"""

class Person(object):
    species = 'linhnt' # class attribute

    #initializer <=> constructor
    def __init__(self, name):
        self.name = name # instance attribute

    def __str__(self):
        return self.name

    def rename(self, renamed):
        self.name = renamed
        print('Now, my name is {}'.format(self.name))

""" Properties

"""
    
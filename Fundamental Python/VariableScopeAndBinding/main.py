""" Nonlocal variables
- Allow assign to variables in an outer scope --> "but not global scope"

"""
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

res = counter()
print(res())

""" Global variables
- variables are inside functions --> are considered local <==> they appear in the left side of a assignment.
- Else, --> global variables.

"""
x = 'Hi'
def read_x():
    print(x) # x is referenced, therefore assumed global

def read_y():
    y = 'Hello'
    print(y)

read_x()
read_y()

def change_x():
    global x
    x = "Hi Vietnam"

    l = 10
    print(x)
    print(globals().keys())
    print(locals().keys())

change_x()
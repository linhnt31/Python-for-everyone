""" Inheritance
- A new class can be derived from an *existing class*

- *super()* is used to call the __init__() method of BaseClass 
    + Especially, calling any overridden method of the BaseClass
"""

class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h 

    def perimeter(self):
        return 2 * (self.w + self.h)

class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super().__init__(s, s)
        self.s = s 
    
a = Square(2)
print(a.area())
print(a.perimeter())

print('Square is subclass of Rectangle: ?', issubclass(Square, Rectangle))
print('a is instance of Square class: ?', isinstance(a, Square))

### *Mokey Patching*: adding a new variable or method to a class after it is been defined

class A:
    def __init__(self, num):
        self.num = num
    
    def __add__(self, other):
        return (self.num + other.num)
    
def get_num(self):
    return self.num

foo = A(42)
# Add a method in A
A.get_num = get_num

print(foo.get_num())
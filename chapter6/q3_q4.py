from abc import ABC, abstractmethod
from math import pi

# Q3:
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def circ(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return self.r * self.r * pi

    @property
    def circ(self):
        return 2 * pi * self.r

# What parts of the original code did you have to touch?
# Everything, i.e. the interface and the 2 classes

# Q4:

class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def area(self):
        return self.w * self.h

    @property
    def circ(self):
        return 2 * (self.w + self.h)


class Square(Rect):
    def __init__(self, l):
        super().__init__(l, l)


# What code did you have to touch in Haskell vs. C++ or Java
# I had to touch no existing code in Python, in Haskell I would have had to change the circ and area functions as well as Shape

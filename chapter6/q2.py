from abc import ABC, abstractproperty
from math import pi

class Shape(ABC):

    @abstractproperty
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return self.r * self.r * pi

class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    @property
    def area(self):
        return self.w * self.h



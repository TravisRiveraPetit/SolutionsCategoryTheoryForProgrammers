class WrongTypeException(Exception):
    pass

def either(left, right):
    class Klass:
        def __init__(self, item):
            self.item = item
            if not self.is_left and not self.is_right:
                raise WrongTypeException

        @property
        def is_left(self):
            return type(self.item).__name__ == left.__name__

        @property
        def is_right(self):
            return type(self.item).__name__ == right.__name__

        def __str__(self):
            s = 'Left: ' if self.is_left else 'Right: '
            s += str(self.item)
            return s

    return Klass

int_or_str = either(int, str)

x = int_or_str(2)
y = int_or_str('hello')
try:
    int_or_str(3.4)
except WrongTypeException:
    print('ok')


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

vec2_or_float = either(Vec2, float)

pi = vec2_or_float(3.14)
half_half = vec2_or_float(Vec2(.5, .5))


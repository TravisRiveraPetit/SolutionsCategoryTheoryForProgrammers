from math import sqrt

EMPTY = object()  # sentinel object

class Optional:
    def __init__(self, obj=EMPTY):
        self.__obj = obj

    @property
    def value(self):
        return self.__obj

    @property
    def is_valid(self):
        return self.__obj is not EMPTY

    def __str__(self):
        x = str(self.value) if self.is_valid else ''
        return f'Optinal [{x}]'


def partial_function_composition(f, g):
    def comp(x):
        gx = g(x)
        if gx.is_valid and f(gx.value).is_valid:
            return f(gx.value)
        return Optional()
    return comp

def identity(x):
    return Optional(x)

def safe_root(x):
    if x >= 0:
        return Optional(sqrt(x))
    return Optional()

def safe_reciprocal(x):
    if x != 0:
        return Optional(1/x)
    return Optional()


comp = partial_function_composition(safe_root, safe_reciprocal)
print(comp(1))  # 1
print(comp(0))  # null
print(comp(-2))  # null
print(comp(1/9))  #  3

print('')
print('Identity test:')
print('')
comp = partial_function_composition(identity, comp)
print(comp(1))  # 1
print(comp(0))  # null
print(comp(-2))  # null
print(comp(1/9))  #  3


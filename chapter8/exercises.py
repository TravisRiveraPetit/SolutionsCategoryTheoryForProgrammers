bifunctor = lambda f: lambda g: lambda bicomp: lambda x: lambda y: bicomp(f(x))(g(y))

f = lambda x: x * x
g = lambda x: str(x) + str(x)

bicomp = lambda x: lambda y: [y for _ in range(x)]

x = bifunctor(f)(g)(bicomp)(3)('test')
print(x)

# in this example:
#
#                    f
#        int -----------------> int
#         |                     |
#         |                     |
#         |                     |
#         v         F f g       v
#      F int int -----------> F int str
#         ^                     ^
#         |                     |
#         |                     |
#         |          g          |
#        int -----------------> str
#
# Where
# F int int = int -> str
# F int str = [str]
# F f g = \x :: (int, str). repeat snd x fst x times


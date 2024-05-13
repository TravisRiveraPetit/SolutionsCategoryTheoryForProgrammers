# 7.3)

composition = lambda f, g : lambda x: f(g(x))
F = lambda a_to_b: lambda r_to_a: composition(a_to_b, r_to_a)

# Example:
#                            f
#                     a -----------> b

#                            |
#                            |
#                            v

#                r -> a -----------> r -> b
#                           F f
#
#                  So if f :: int -> str is fixed, and r = List [int], then
#                  F f :: (List[int] -> int) -> (List[int] -> str)
#                  F f g [x_1 ... x_n] = f o g (x_1 ... x_n)
#

f = lambda x: str(x) + '!'
g = sum
x = F(f)(g)([1,2,6])
print(x)


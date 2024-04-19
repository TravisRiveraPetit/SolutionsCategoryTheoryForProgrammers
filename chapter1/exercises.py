from typing import Any, Callable, TypeVar, Tuple, List

A = TypeVar('A')
B = TypeVar('B')
C = TypeVar('C')

# 1: Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite language happens to be Haskell)
def identity(x: Any) -> Any:
    return x

print(identity(4))


#2: Implement the composition function in your favorite language. It takes two functions as arguments and returns a function that is their composition
def compose(f: Callable[[A], B], g: Callable[[B], C]) -> Callable[[A], C]:
    return lambda x: g(f(x))

def f(x: str) -> int:
    return len(x)

def g(x: int) -> Tuple[int, int, int]:
    return (x, x+1, x+2)

print(compose(f, g)('hello world'))


#3: Write a program that tries to test that your composition function respects identity.
def is_identity(f: Callable[[A], B], test_cases: List[A]) -> bool:
    for x in test_cases:
        if f(x) != x:
            return False
    return 'maybe'

print(is_identity(lambda x: x, [1,2,3,4]))


#4: Is the world-wide web a category in any sense? Are links morphisms?
# Yes?

#5: Is Facebook a category, with people as objects and friendships as morphisms?
# Yes?

#6: When is a directed graph a category?
# Let G = (V, E) be a directed graph.
# G is a category if forall v in V we have (v, v) in E. (i.e. the graph is reflexive) and if
# for all u, v, w in V: if (u, v) in E then (v, w) in E (i.e. the graph is transitive)

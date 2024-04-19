from time import time
import random
from typing import Callable

#1: Define a higher-order function (or a function object) memoize in your favorite language.
# This function takes a pure function f as an argument and returns a function that behaves almost exactly like f,
# except that it only calls the original function once for every argument,
# stores the result internally, and subsequently returns this stored result every time it’s called with the same argument.
# You can tell the memoized function from the original by watching its performance.
# For instance, try to memoize a function that takes a long time to evaluate.
# You’ll have to wait for the result the first time you call it,
# but on subsequent calls, with the same argument, you should get the result immediately

def memoize(f: Callable) -> Callable:
    def memoized_f(*args, **kwargs):
        if not hasattr(memoized_f, "cache"):
            memoized_f.cache = {}

        key = (args, tuple(kwargs.items()))

        if key in memoized_f.cache:
            return memoized_f.cache[key]

        result = f(*args, **kwargs)
        memoized_f.cache[key] = result
        return result

    return memoized_f


def fib(n):
    if n <= 0:
        return 1
    return fib(n-1) + fib(n-2)

print('Question 1:')
start = time()
fib(30)
fib(30)
fib(30)
print(time() - start)

start = time()
g = memoize(fib)
g(30)
g(30)
g(30)
print(time() - start)


#2: Try to memoize a function from your standard library that you normally use to produce random numbers. Does it work?

# Of course not, for memoization to work the function must be pure, in particular it must be deterministic.
# Using this will make it return the same value everey time.

x = memoize(random.random)
print('Question 2:')
print(x())
print(x())
print(x())


#3: Most random number generators can be initialized with a seed.
# Implement a function that takes a seed, calls the random number generator with that seed, and returns the result.
# Memoize that function. Does it work?

# It depends on what you mean by 'it working'. It works in the sense that, for a different seeds, we will get different random numbers.
# However if we run the function twice on the same seed, we get the same output twice.
# this is because, for a given seed, an RNG constructs a well-defined determistic sequence x1, x2, x3, ...
# Calling random once returns x1, calling it again returns x2, then x3 and so on.
# But by resetting the seed each time, we return x1 every time we call the function with the same seed.

@memoize
def make_random_with_seed(seed):
    random.seed(seed)
    return random.random()

print('Question 3:')
print(make_random_with_seed(123))
print(make_random_with_seed(123))

print(make_random_with_seed(321))
print(make_random_with_seed(321))

#4: Which of these C++ functions are pure?
# Try to memoize them and observe what happens when you call them multiple times: memoized and not.

# (a) pure
# (b) Not pure sice it is not deterministic, it can return any unicode character.
# If we memoize it will always return the same first character. Similar to what happens with question 2.
# (c) Not pure since it has side effects. The memoized function will behave correctly because the side effects are benign.
# (d) Very un-pure because it is both nondeterministic and has side effects.

#5: How many different functions are there from Bool to Bool? Can you implement them all?

true = lambda x: True
false = lambda x: False
neg = lambda x: not x
id_ = lambda x: x

# If we consider _|_ (bottom) to be of type Bool (as is the case in Haskell), we get a total of 3^3 = 27 functions.
# We can easy enumerate them in base 3 like this:
# 000
# 001
# 002
# 010
# 011
# 012
# 020
# ...

# WLOG we can assume that 0 = False, 1 = True, 2 = _|_
# So here a string xyz can be intrepreted as False -> x, True -> y, _|_ -> z


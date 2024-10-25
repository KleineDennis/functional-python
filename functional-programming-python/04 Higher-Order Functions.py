# %%
"""
    # Classic "FP-style"
    transformed = map(tranformation, iterator)
    # Comprehension
    transformed = (transformation(x) for x in iterator)

    # Classic "FP-style"
    filtered = filter(predicate, iterator)
    # Comprehension
    filtered = (x for x in iterator if predicate(x))
"""

# %%
from functools import reduce
import operator 

it = range(10)
total = reduce(operator.add, it, 0) # total = sum(it)
print(total)

# %%
add5 = lambda n: n+5
reduce(lambda l,x: l+[add5(x)], range(10), list())

# %%
isOdd = lambda n: n%2
reduce(lambda l, x: l+[x] if isOdd(x) else l, range(10), [])
l = filter(isOdd, range(10))
print(list(l))

# %%
def compose(*funcs):
    """Return a new function s.t. compose(f,g,...)(x) == f(g(...(x)))"""
    def inner(data, funcs=funcs): 
        result = data
        for f in funcs: 
            result = f(result)
        return result 
    return inner

times2 = lambda x: x*2
minus3 = lambda x: x-3
mod6 = lambda x: x%6
f = compose(minus3, times2, mod6)
print(f(10))
all(f(i) == ((i-3)*2)%6 for i in range(1000000))

# %%
from functools import reduce

compose0 = lambda *F: reduce(lambda f, g: lambda x: f(g(x)), F)

def compose1(*fs):
    return reduce(lambda f, g: lambda x: f(g(x)), fs)

def _compose2(f, g):
    return lambda *a, **kw: f(g(*a, **kw))

def compose2(*fs):
    return reduce(_compose2, fs)

def compose3(*funcs):
    return lambda x: reduce(lambda acc, f: f(acc), reversed(funcs), x)

f1 = lambda x: x+3
f2 = lambda x: x*2
f3 = lambda x: x-1
g = compose0(f1, f2, f3)
assert(g(7) == 15)

# %%
from functools import partial
import operator
from math import factorial

all_pred = lambda item, *tests: all(p(item) for p in tests) 
any_pred = lambda item, *tests: any(p(item) for p in tests)

is_prime = lambda x: factorial(x - 1)  % x == x - 1
is_lt100 = partial(operator.ge, 100)
is_gt10 = partial(operator.le, 10)

predicates = (is_lt100, is_gt10, is_prime)
all_pred(71, is_lt100, is_gt10, is_prime)
any_pred(107, *predicates)
# %%

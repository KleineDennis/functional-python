# %%
def get_primes():
    candidate = 2 
    found = [] 
    while True:
        if all(candidate % prime != 0 for prime in found): 
            yield candidate
            found.append(candidate)
        candidate += 1

from collections.abc import Sequence 
class ExpandingSequence(Sequence):
    def __init__(self, it): 
        self.it = it
        self._cache = []
    def __getitem__(self, index): 
        while len(self._cache) <= index: 
            print(f"len: {self.__len__()}")
            self._cache.append(next(self.it))
        return self._cache[index] 
    def __len__(self):
        return len(self._cache)

primes = ExpandingSequence(get_primes())
for _, p in zip(range(10), primes):
    print(p, end=" ")

# %%
print(primes[10])
print(primes[5])
print(primes.__getitem__(5))
print(primes.__len__())
print(primes[100])
print(len(primes))

# %%
from collections.abc import Iterable 
class Fibonacci(Iterable):
    def __init__(self): 
        self.a, self.b = 0, 1 
        self.total = 0
    def __iter__(self): 
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b 
        self.total += self.a
        return self.a
    def running_sum(self): 
        return self.total

fib = Fibonacci()
fib.running_sum()
for _, i in zip(range(10), fib):
    print(i, end=" ")
fib.running_sum()
next(fib)
fib.running_sum()

"Since state‐ fulness is for object-oriented programmers, in a functional pro‐ gramming style we will generally avoid classes like this."
# %%
def fibonacci():
    a,b = 1,1
    while True:
        yield a
        a, b = b, a+b

from itertools import tee, accumulate

s, t = tee(fibonacci())
pairs = zip(t, accumulate(s))
for _, (fib, total) in zip(range(10), pairs):
    print(fib, total)

# %%

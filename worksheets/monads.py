# %%
class Maybe:
    def __init__(self, value):
        self._value = value

    def bind(self, func):
        if self._value is None:
            return Maybe(None)
        else:
            return Maybe(func(self._value))

    def orElse(self, default):
        if self._value is None:
            return Maybe(default)
        else:
            return self

    def unwrap(self):
        return self._value

    def __or__(self, other):
        return Maybe(self._value or other._value)

    def __str__(self):
        if self._value is None:
            return 'Nothing'
        else:
            return 'Just {}'.format(self._value)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, Maybe):
            return self._value == other._value
        else:
            return False

    def __ne__(self, other):
        return not (self == other)

    def __bool__(self):
        return self._value is not None

def add_one(x):
    return x + 1

def double(x):
    return x * 2

result = Maybe(3).bind(add_one).bind(double)
print(result)  # Just 8

result = Maybe(None).bind(add_one).bind(double)
print(result)  # Nothing

result = Maybe(None).bind(add_one).bind(double).orElse(10)
print(result)  # Just 10

result = Maybe(None) | Maybe(1)
print(result) # Just 1

# %%
class State:
    def __init__(self, state):
        self.state = state

    def __call__(self, value):
        return (self.state[1], State((self.state[0] + 1, value)))

# create a stateful computation that counts the number of times it is called
counter = State((0, 0))

# call the computation multiple times and print the current count
for i in range(5):
    result, counter = counter(i)
    print(f"Computation result: {result}, count: {counter.state[0]}") 


# %%
class IO:
    def __init__(self, effect):
        self.effect = effect

    def __call__(self):
        return self.effect()

def read_file(filename):
    def read_file_effect():
        with open(filename, 'r') as f:
            return f.read()

    return IO(read_file_effect)

def print_contents(contents):
    def print_effect():
        print(contents)

    return IO(print_effect)

# chain the IO operations manually
contents = read_file('example.txt')()
print_contents(contents)()

# %%
class CallMeAnything:

    class _Callable:
        def __init__(self, instance, method):
            self._instance = instance
            self._method = method

        def __call__(self, *args, **kwargs):
            # call original instance fallback method
            return self._instance._fallback_method(self._method, args, kwargs)

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        # no method or attribute found in this instance -> create fallback callable
        return CallMeAnything._Callable(self, key)

    def _fallback_method(self, method_name, args, kwargs):
        print(f"called {method_name} with args={args} and kwargs = {kwargs})")


if __name__ == "__main__":
    o = CallMeAnything()
    o.hello("world")
    o.foo(42, bar="foobar")

# %%
from datetime import datetime
from typing import Optional

def maybe_magic_function() -> Optional[str]:
    return "magic" if datetime.now().day == 1 else None

magic = maybe_magic_function()

# %%

def magic_function() -> Maybe:
    return Just("magic") if datetime.now().day == 1 else Nothing()

match magic_function():
    case Just(value=magic):
       print(f"{magic=}")
    case Nothing():
       print("no magic")
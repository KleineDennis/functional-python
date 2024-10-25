# %%
from collections.abc import Sequence, Callable
from typing import List, Tuple

def foldr(seq: Sequence[int], op: Callable[[int, int], int], init: int) -> int:
    """Recursive reduce operation, fold from right to left."""
    if len(seq) == 0:
        return init
    return op(seq[0], foldr(seq[1:], op, init))


def test_foldr() -> None:
    assert foldr([2, 3, 5, 7], lambda x, y: x + y, 0) == 17
    assert foldr([1, 2, 3, 4], lambda x, y: x * y, 1) == 24
# %%
#"class is “data with operations attached” while a closure is “operations with data attached.”
from dataclasses import dataclass

#@dataclass(frozen=True)
class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, m):
        return self.n + m
add5_i = Adder(5)
add5_i.n #= 10
add5_i(10)

# %%
def make_adder(n): 
    def adder(m):
        return m + n 
    return adder
add5_f = make_adder(5)
add5_f(10)

# %%
adders = []
for n in range(5):
    adders.append(lambda m, n=n: m+n)

[adder(10) for adder in adders]
n = 10 #resign doesn't matter with n=n
[adder(10) for adder in adders]

add4 = adders[4]
add4(10, 100)

# %%
class Car:
    def __init__(self):
        self._speed = 100
    @property
    def speed(self):
        print("Speed is", self._speed) 
        return self._speed
    @speed.setter
    def speed(self, value): 
        print("Setting to", value) 
        self._speed = value

car = Car()

# %%
import functools, operator
class Math:
    def __init__(self):
        self.__speed = 100
    def product(*nums):
        return functools.reduce(operator.mul, nums)
    def power_chain(*nums):
        return functools.reduce(operator.pow, nums)

Math.product(3,4,5)
Math.power_chain(3,4,5)
m = Math()
#m.product(3,4,5)
m.__dict__
m._Math__speed

# %%
def get_primes():
    "Simple lazy Sieve of Eratosthenes"
    candidate = 2 
    found = [] 
    while True:
        if all(candidate % prime != 0 for prime in found): 
            yield candidate
            found.append(candidate)
        candidate += 1

primes = get_primes()
#next(primes), next(primes), next(primes)

#print(list(zip(range(10), primes)))

for _, prime in zip(range(10), primes):  #just 10
    print(prime, end=" ")

#for prime in primes:  #infinite
#    print(prime, end=" ")

# %%
from dataclasses import dataclass

@dataclass(frozen=True)
class Thing:
    _win_cases = [['rock','scissor'], ['scissor','paper'], ['paper','rock']]

@dataclass(frozen=True)
class Rock(Thing):
    name = "rock"
    
    def beats(self, other):
        return ([Rock.name, other.name] in super()._win_cases)

@dataclass(frozen=True)
class Paper(Thing):
    name = "paper"
    def beats(self, other):
        return ([Paper.name, other.name] in super()._win_cases)

@dataclass(frozen=True)
class Scissor(Thing):
    name = "scissor"
    def beats(self, other):
        return ([Scissor.name, other.name] in super()._win_cases)

def beats2(x, y):
    return x.beats(y) 

Thing._win_cases = []
rock, paper, scissor = Rock(), Paper(), Scissor()

rock.beats(scissor) 
# print(beats2(rock, scissor))
# print(beats2(paper, rock))
# print(beats2(rock, scissor))

# %%
class Thing: pass
class Scissor(Thing):
    @staticmethod
    def beats(x: Thing) -> bool:
        match x:
            case Paper():  
                return True
        return False

class Paper(Thing):
    @staticmethod 
    def beats(x: Thing) -> bool:
        match x:
            case Rock():
                return True
        return False
    
class Rock(Thing):
    @staticmethod
    def beats(x: Thing) -> bool:
        match x:
            case Scissor():
                return True
        return False

print(Rock.beats(Scissor()))
print(Scissor.beats(Paper()))
print(Paper.beats(Rock()))
print(Paper.beats(Scissor()))

# %%
# from dataclasses import dataclass, replace

# @dataclass(frozen=True)
# class Thing:
#     win_cases = [['rock','scissor'], ['scissor','paper'], ['paper','rock']]

#     def __init__(self, name):
#         self.name = name

#     def beats(self, other):
#         return ([self.name,other] in Thing.win_cases)

# Thing.win_cases = []
# p = Thing("paper")
# s = Thing("scissor")
# r = Thing("rock")

# p.beats("paper")
# r.beats("scissor")

# %%

class Student: 
    def __init__(self, name, course): 
        self.__name = name 
        self.__course = course
        self.__id = "3453453452345"
        
    @property
    def studentid(self):
        return self.__id

    @studentid.setter 
    def studentid(self, id): 
        self.__id = id 
        
s = Student("Anita", "MBA") 
print(s.studentid)
s.studentid = "123" 
print(s.studentid)
#s.__course = "None"
print(s.__course)

# %%
class Employee_: 
	def __init__(self, basesalary, yearsofworking): 
		self.basesalary = basesalary 
		self.yearsofworking = yearsofworking 
		self._salary = 0
	
	@property
	def salary(self): 
		return self._salary 

	@salary.setter 
	def salary(self, salary): 
		self._salary = salary 

amit = Employee_(20000, 5) 
amit.salary = 10000
print(amit.basesalary, amit.yearsofworking, amit.salary) 

# %%
class Person:
    def __init__(self, name, age):
        self._protected_attribute = 'This is a protected attribute.'
        self.name = name
        self.age = age


class Employee(Person):
    def display_protected_attribute(self):
        print(self._protected_attribute)

employee = Employee('Jane Doe', 25)
employee.display_protected_attribute()  # This is a protected attribute.
print(employee._protected_attribute)    # This is a protected attribute.

# %%

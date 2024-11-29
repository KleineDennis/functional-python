#%%
# 3. Simple Data Structures

class PersonClass:
    def _init_(self, id):
        self.id = id

person = {"id": 10, "name": "Shaun", "age": 123, "hair": "brown"}
print(person)

person_ = { **person, "name": "John"}
print(person_)

# %%
from collections import defaultdict

# Create a defaultdict with a default value of an empty list
my_dict = defaultdict(list)

# Add elements to the defaultdict
my_dict['fruits'].append('apple')
my_dict['vegetables'].append('carrot')

# Print the defaultdict
print(my_dict)

# %%
from collections import defaultdict

given  = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


# defaultdict(list, given).get("brand1")
dict(given).get("brand")

# %%
import os
print(__file__)
print(os.path.join(os.path.dirname(__file__), '..'))
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.abspath(os.path.dirname(__file__)))

# %%
numbers = [1,2,3,4,5,6,7,8,9,10]

def double(x):
    return x*x

def is_even(x):
    return x % 2 == 0

doubled_numbers = list(map(double, numbers))
doubled = list(double(x) for x in numbers)
evens = list(filter(is_even, doubled))
evens2 = [x for x in numbers if x % 2 == 0]
doubled_evens = [double(x) for x in numbers if x % 2 == 0]
is_any_even = any(map(is_even, numbers))
is_all_even = all(map(is_even, numbers))

# print(doubled)
# print(evens2)
# print(is_any_even)
# print(is_all_even)
print(doubled_evens)


# %%
number_1 = [1,2,3]
number_2 = [5,6,7]
combines_numbers = [*number_1, *number_2]
print(combines_numbers)

# %%
person = {"name": "Shaun", "age": 123, "hair": "brown"}
update_person = {**person, "age": 55}

print(update_person)
# %%

# %%
import csv

with open('/Users/denniskleine/Downloads/techcrunch.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

# %%
def csv_reader1(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result

def csv_reader2(file_name):
    for row in open(file_name, "r"):
        yield row

csv_gen = csv_reader2("/Users/denniskleine/Downloads/techcrunch.csv")
row_count = 0
for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

# %%
csv_gen = (row for row in open("/Users/denniskleine/Downloads/techcrunch.csv", "r"))
row_count = 0
for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")

# %%
nums_squared_lc = [num**2 for num in range(5)]
nums_squared_gc = (num**2 for num in range(5))
print(nums_squared_lc)
print(nums_squared_gc)
print(nums_squared_gc.__next__())
print(nums_squared_gc.__next__())

# %%
import sys

nums_squared_lc = [i ** 2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))

nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

# %%
def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
print(next(multi_obj))

# %%
from statistics import mean
from itertools import count
#count = count().__next__
c = count(0)

file_name = "/Users/denniskleine/Downloads/techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
funding = (
    #(int(company_dict["raisedAmt"]), next(c))[0]
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
#total_series_a = sum(funding)
#print(f"Total series A fundraising: ${total_series_a}")
#c = count()
#print(c)
#m = sum(funding) / next(c)
#print(m)

print(mean(funding))

# %%
import itertools
count = itertools.count().__next__
s = sum((count(), x)[1] for x in range(10) )
print(s/count())

# %%
strings = ['the', 'joy', 'of', 'coding', 'Python', 'should',
'be', 'in', 'seeing', 'short', 'concise',
'readable', 'classes', 'that', 'express', 'a',
'lot', 'of', 'action', 'in', 'a', 'small', 'amount',
'of', 'clear', 'code', 'not', 'in', 'reams', 'of',
'trivial', 'code', 'that', 'bores', 'the', 'reader',
'to', 'death']

def sumcount(it):
    sum = 0;
    count = 0;
    for x in it:
        sum += x
        count += 1
    return sum, count

s = filter(lambda x : x not in ('a', 'the'), strings)
total, count = sumcount(map(len, s))
average = total/count
print(average)

# %%
file_name = "/Users/denniskleine/Downloads/techcrunch.csv"
lines = (line for line in open(file_name))
list_line = (s.rstrip().split(",") for s in lines)
cols = next(list_line)
company_dicts = (dict(zip(cols, data)) for data in list_line)
#print(list(company_dicts))
funding = (
    int(company_dict["raisedAmt"])
    for company_dict in company_dicts
    if company_dict["round"] == "a"
)
def sumcount(it):
    sum = 0
    count = 0
    for x in it:
        sum += x
        count += 1
    return sum, count

total, count = sumcount(funding)
average = total / count
print(average)

# %%

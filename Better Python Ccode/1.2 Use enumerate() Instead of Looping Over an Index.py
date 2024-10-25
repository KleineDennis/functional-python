# %%
items = [1,2,3,4,5]
def process(x, i):
    print(x, i)

for i in range(len(items)):
    process(i, items[i])

# %%
for item in items:
    process(None, item)

# %%
for i, item in enumerate(items):
    process(i, item)

# %%

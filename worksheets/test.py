#%%
# 3. Simple Data Structures

class Persion:
    def _init_(self, id):
        self.id = id

person = {"id": 10, "name": "Shaun", "age": 123, "hair": "brown"}
print(person)

person_ = { **person, "name": "John"}
print(person_)



# %%

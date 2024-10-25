# %%
# source = <some identifier for how we generate data>
from random_word import RandomWords
r = RandomWords()
#print(r.get_random_word())

# %%
words = []
#while True:
for _ in range(1000):    
    word = r.get_random_word()
    if word is None:
        break
    words.append(word)
print(f"{len(words):,}") # -> 267,752

# %%
def word_number(word):
    magic = 0
    for letter in word:
        magic += 1 + ord(letter) - ord('a')
    return magic

# %%

# %%
#words = <regenerated list from another source>
import matplotlib.pyplot as plt
plt.plot([word_number(word) for word in words]) 
plt.title(f"Magic values of {len(words):,} generated words") 
plt.show()

# %%
from random_word import RandomWords
import matplotlib.pyplot as plt

def word_number(word):
    magic = 0
    for letter in word:
        magic += 1 + ord(letter) - ord('a')
    return magic

# def word_numbers(src):
#     while (word := src.get_random_word()) is not None:
#         yield word_number(word)

def word_numbers(src):
    for _ in range(1000):
        word = src.get_random_word()
        yield word_number(word)

source2 = RandomWords()
magic_nums = list(word_numbers(source2))
plt.plot(magic_nums)
plt.title(f"Magic values of {len(magic_nums):,} generated words")
plt.show()
# %%

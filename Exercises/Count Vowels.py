"""
Write a function count_vowels(text) that counts how many vowels (a, i, e, o, u)
are in the string.
"""

def count_vowels(text):
    text = input("Please enter a sentence: ")
    l = text.lower()
    vowels = "aioue"
    c = 0
    for i in l:
        if i in vowels:
            c+=1
    print(f"There are {c} vowels in the string.")
    

print(count_vowels("Hello"))
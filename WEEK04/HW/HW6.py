str1 = input("Please enter a sentence: ")
str2 = input("Please enter a sentence: ")

"""
Here we have to make 2 variables, first one i, which is the index of 
every word in our sentence. And the other one is match, which will decrease 
when the program finds a matching word in sentences. At first, both of these variables 
equalls to 0.
"""

i = 0
match = 0

while i < len(str1):
    if str1[i] == str2[i]:
        match += 1
    i += 1

print(f"Matchings are = {match}")
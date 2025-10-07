import itertools
from itertools import combinations
import copy

"""
first we are going to ask the user to enter a sentence so we can use the words in it to make combinations. we create 
an empty list to add the combined words in the list. We then use split built-in function to make a list of the inputed sentence.
Then we create a for loop, for 2 - 4 combined list of words. and then we append the collections to the empty list. 
"""

sentence = input("Please enter a word or a sentence: ")
list2 = []
s = sentence.split()
for w in [2, 3, 4]:
    for i in combinations(s, w): 
        list2.append(list(i))

shallow = list2.copy()
deep = copy.deepcopy(list2)

if list2:
    list2[0][0] = "maktab137"

print("All combinations: ", list2)
print("All combinations with shallow copy: ", shallow)
print("All combinations with deep copy: ", deep)



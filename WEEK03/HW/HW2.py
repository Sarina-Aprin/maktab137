import copy
"""
So first we are going to create a decorator for cache. So that everytime our program takes the same sentence as before, it doesn't
spend memory for it and return it from cache. Then we are going to make afunction, to count the words of the given sentence but 
first, we are going to write codes for the conditions. So, first we use .lower to make the characters lowercase and then we 
write a variable called punctuations so that the for loop goes over it and if it found any of them in the sentence it replaces them with "".
Then we use .split to make the sentence a list and make a dict called repeat so that everytime a word is repeated the program is going 
to add it to the empty dict and tell us how many times it had been repeated. We also make the output of the list lowercase so that it matches 
the input sentence. 
"""

def saving(func):
    cache = {}
    def wrapper(sentence, words):
        key = str(words)
        if key in cache: 
            print("Returning from cache")
            return copy.deepcopy(cache[key])
        result = func(sentence, words)
        cache[key] = copy.deepcopy(result)
        print("Cache created")
        return result
    return wrapper

@saving
def word_count(sentence, list1):
    sentence1 = sentence.lower()
    punctuation = "?.,/!"
    for char in sentence1:
        if char in punctuation:
            sentence1 = sentence1.replace(char, "")
            
    
    sentence1 = sentence1.split()
    repeat = {}
    for word in list1:
        x = word.lower()
        repeat[x] = sentence1.count(x)

    return repeat 

print(word_count("I Sarina sarina Aprin aprin", ["SaRiNa", "aprin", "I"]))
print(word_count("I Sarina sarina Aprin aprin", ["SaRiNa", "aprin", "I"]))
print(word_count("You are Sarina Aprin", ["SaRiNa", "aprin", "I"]))
print(word_count("You are Sarina Aprin", ["SaRiNa", "aprin", "I"]))
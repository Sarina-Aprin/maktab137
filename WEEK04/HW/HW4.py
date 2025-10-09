"""
recursive function
"""

def nested_sum(lst):
    count = 0
    for i in lst:
        if isinstance(i, list): #Check if i is a list
            count += nested_sum(i)
        else:
            count += i
    return count

print(nested_sum([1, [2, 3], [4, [5]]])) 

"""
The isinstance() function returns True if the specified object is of the specified type, 
otherwise False. As we want to check if what we are iterating over is a list or not,
we need isinstance. And for iterating over a list we use for. 
"""
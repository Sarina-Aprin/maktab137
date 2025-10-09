from collections import Counter

"""
This function has to show which element of a list is repeated more than once.
"""

a = [1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 8, 2]
def repeatition(a):
    c = Counter(a)
    return c.most_common(1)[0][0]
print(repeatition(a))


"""
So here we used a new class called counter. why did we use (1)[0][0]?
Counter, makes the list into a dict like this
Counter({9:1, 8:2, 7:2, 6:1, 5:1, 4:1, 3:1, 2:2, 1:3})
when we use the method most_common
the output will be a list of tuple in order of the most common elements
[(1:3), (2:2), (7:2), (8:2), (3:1), (4:1), (5:1), (6:1), (9:1)]
so when we write (1) it means, give me just one of the most commons: [(1:3)]
with [0] we get to the one and only tuple: (1:3)
as we want to know which element is the most common one and we don't want to know 
how many times it has occured, we use [0] which is index 1 of the tuple to get the element out: 1
"""
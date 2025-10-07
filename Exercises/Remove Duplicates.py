"""
Write a function remove_duplicates(lst) that removes duplicates from a list and returns a new one.
"""

lst = [1, 1, 1, 4, 8, 9, 15]

def remove_duplicates(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

print(remove_duplicates(lst))

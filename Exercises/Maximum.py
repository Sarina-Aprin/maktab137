"""
Write a function find_max(numbers) that returns the largest number in a list.
"""

list1 = [14, 100, 50, 75, 45, 62, 115]

def find_max(list1):
    for i in list1:
        if max(list1) == i:
            print(f"The maximum number in list is {i}")

print(find_max(list1))
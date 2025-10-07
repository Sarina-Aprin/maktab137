"""
Write a function is_even(num) that returns True if the number is even, otherwise False.
"""

def is_even(num):
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("True")
    else:
        print("False")
    return is_even

is_even(14)
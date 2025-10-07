"""
Write a function sum_of_digits(num) that returns the sum of all digits in a number.
"""

def sum_of_digits(num):
    num = input("Please enter a number: ")
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)

print(sum_of_digits("12"))
"""
Write a function fizzbuzz(n) that prints numbers from 1 to n, but:
Prints "Fizz" for multiples of 3,
"Buzz" for multiples of 5,
"FizzBuzz" for multiples of both.
"""

def FizzBuzz(num):
    num = int(input("Please enter a number: "))
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")

FizzBuzz(15)
"""
Write a function factorial(n) that returns the factorial of n using recursion.
(If n is 0, return 1)
"""

def factorial(n):
    fact = 1
    n = int(input("Please enter a number: "))
    for i in range(1, n+1):
        if i == 0:
            return 1
        else:
            fact *= i
    print(fact)
    
print(factorial("12"))
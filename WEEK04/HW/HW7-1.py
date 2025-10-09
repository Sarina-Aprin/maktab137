"""
positional only arguments are seperated with / and the values of them can only be
passed to a function as a positional argument. It is useful when the order of arguments
is more important than their names.
"""

def multiply(num1, num2, /):
    return num1 + num2

print(multiply(10, 80)) #90
print(multiply(num2 = 80, num1 = 10)) #TypeError: multiply() got some positional-only arguments passed as keyword arguments
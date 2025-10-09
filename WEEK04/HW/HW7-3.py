"""
This is a calculator. It uses the operators '/ * + -' for given nums.
"""

def calculator(num1: float, num2: float, /, *, operator = str):
    if operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Can not be divided by zero")
        return num1 / num2
    elif operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        raise ValueError("You have used an unsupported operator. You can only use +, -, *, /.")
    
print(calculator(4.5, 5, operator = "*")) #22.5
print(calculator(99, 1.1, operator = "+")) #100.1
print(calculator(55, 0, operator = "/")) #ZeroDivisionError: Can not be divided by zero
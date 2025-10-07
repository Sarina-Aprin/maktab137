"""
Write a function that takes someones name and greets them.
"""

def greet(name):
    name = input("What is your name?: ")
    condition = input(f"Hello {name}! How are you today? ")

    if condition == "Good":
        print("Nice! Have a good day!")
    elif condition == "Not bad":
        print("Hope you have a good day!")
    else:
        print("Then make the rest of the day worth it!")

    return greet

greet("Sarina")
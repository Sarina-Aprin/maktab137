"""
Write a function reverse_string(s) that returns the reversed version of a given string.
"""

def reverse_string(text):
    text = input("Please enter a text: ")
    new_text = ''.join(reversed(text))
    print(new_text)

print(reverse_string("Hello"))
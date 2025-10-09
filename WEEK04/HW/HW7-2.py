"""
keyword only arguments are specified after an * in the function definition. 
They can only be passed to a function as keyword arguments and cannot be 
passed as positional arguments. 
This can be useful in cases where certain arguments have a default value and should be optional.
"""

def id(cn , * , name = "Sarina", age = "22"):
    return f"Your customer number is {cn}. You are {name}. You are {age}."

print(id(12, name = "Amir", age = "35")) #Your customer number is 12. You are Amir. You are 35.
print(id(4, name = "Kolsum", age = "75")) #Your customer number is 4. You are Kolsum. You are 75.
print(id("Arian", cn = "88", age = "40")) #TypeError: id() got multiple values for argument 'cn'
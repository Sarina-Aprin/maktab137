"""
I write the argumants of wrapper, which are our inputs, as args and kwargs 
cause it gives us the ability to save any type of input. 
"""
def makefile(func):
    def wrapper(*args, **kwargs):
        with open("input.txt", "w", encoding="utf-8") as f_input:
            f_input.write(f"args: {args}\n")
            f_input.write(f"kwargs: {kwargs}\n")
        result = func(*args, **kwargs) #This is how we run the main function. func is the inputs we got.

        with open("output.txt", "w", encoding="utf-8") as f_output:
            f_output.write(f"result: {result}\n") #As we want the outputs we write the result of the func.
        return result
    return wrapper

@makefile
def multiply(num1, num2):
    return num1 * num2


multiply(40, 78)
def make_str(func):
    def wrapper(*args, **kwargs):
        args_as_str = [str(arg) for arg in args]
        kwargs_as_str = {key: str(value) for key, value in kwargs.items()}
        print(f"args as strings: {args_as_str}")
        print(f"kwargs as strings: {kwargs_as_str}")
        return func(*args_as_str, **kwargs_as_str)
    return wrapper

def str_len(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, str):
                print(f"Length of args as string is: {len(arg)}")

        for key, value in kwargs.items():
            if isinstance(value, str):
                print(f"Length of kwargs as string is: {len(value)}")
        return func(*args, **kwargs)
    return wrapper

@make_str
@str_len
def greet(name, message):
    return f"{message}, {name}!"

greet(24, message = "I am Sarina Aprin")
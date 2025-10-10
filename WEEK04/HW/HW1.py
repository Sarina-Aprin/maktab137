from datetime import datetime

"""
A decorator with 3 functions is a decorator that has an outer func which makes a 
decorator. This func gets parameters and finally returns the real decorator.
"""

def allowed_time(start, end):
    def activity(func):
        def wrapper(*args, **kwargs):
            right_now = datetime.now().hour
            if start <= right_now < end:
                print("Time is valid. Working on the function...")
                return func(*args, **kwargs)
            else:
                print("Invalid time. You can't work on this function right now.")
        return wrapper
    return activity


@allowed_time(8, 21)
def say_hello():
    print("Hello Sarina!")

say_hello()
from time import time
numbers = [14, 115, 48, 25, 55, 59, 80, 96, 104, 11, 150, 78, 86, 99]
"""
Bubble sort takes a list of numbers, from right to left, it's going to check each number.
If the first number is smaller than next one, it doesn't swap it. But if it's not, it swaps 
the numbers so that the smaller numbers are on the right and the greater numbers are on the left.
I added a performance decorator too so that we can track the time that the process takes.
"""
def performance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"It took {t2-t1}s")
        return result
    return wrapper

@performance
def bubble_sorted(numbers):
    """
    first we put the list length in a variable called n. 
    then we write a for loop that takes each number and 
    gives it to j loop so that it can compare it to next number.
    if the number war bigger than next one, it's going to swap it.
    else it moves to the next number. 
    """
    n = len(numbers)
    for i in range(n):
        for j in range(n-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j] 
    print(numbers)

bubble_sorted(numbers)

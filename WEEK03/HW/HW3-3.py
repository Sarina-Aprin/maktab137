import time

numbers = [14, 115, 48, 25, 55, 59, 80, 96, 104, 11, 150, 78, 86, 99]

def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    pivot = list1[0] 
    smaller = []
    greater = []
    for i in list1:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            smaller.append(i)
    return quick_sort(smaller) + [pivot] + quick_sort(greater)

start = time.time()
print(quick_sort(numbers))
end = time.time()
print(end - start)
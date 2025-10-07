import time

numbers = [14, 115, 48, 25, 55, 59, 80, 96, 104, 11, 150, 78, 86, 99]


def merge(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    list3 = []
    i = j = 0
    while i < len1 and j < len2:
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i+=1
        else:
            list3.append(list2[j])
            j+=1
    list3 += list1[i:]
    list3 += list2[j:]
    return list3


def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers
    else:
        mid = len(numbers) // 2
        left = numbers[:mid]
        right = numbers[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

start = time.time()
print(merge_sort(numbers))
end = time.time()
print(end - start)
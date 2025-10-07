# Exercise = Check for duplicatesc in a list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []

for letters in some_list:
    if some_list.count(letters) > 1:
        if letters not in duplicates:
            duplicates.append(letters)
    
print(duplicates)
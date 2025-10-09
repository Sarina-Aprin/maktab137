def number_info(n):
    number = int(input("Enter a number: "))
    if number < 0:
        print("Number has to be greater than 0.")
        return
    for number in range (1, n + 1):
        print(number)
    double = lambda x : x * 2 
    powered = lambda x : x ** 2 
    new_dict = {}
    for i in range(1, n+1):
        if i % 2 != 0:
            new_dict[i] = double(i)
        else:
            new_dict[i] = powered(i)
    values_list = list(map(lambda x: x, new_dict.values()))
    print(values_list)

print(number_info(10))
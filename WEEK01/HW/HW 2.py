n = int(input("Enter a number: "))
result = 0

for i in range(1, n):
    if n % i == 0:
        result = result + i 

if result == n:
    print("Yes!")
else:
    print("No!")
user_name = str(input("What is your name?: "))
score = int(input("Score?: "))

if score > 90:
    print(f"{user_name} : Great!")

elif 70 <= score < 90:
    print(f"{user_name} : Good!")

else: 
    print(f"{user_name} : Needs improvement.")
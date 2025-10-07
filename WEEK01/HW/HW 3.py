Temperature = int(input("What is the weather temperature today?: ")) 

if Temperature < 10: 
    print("The weather is cold.")

elif 10 < Temperature < 25:
    print("The weather is mild.")

else: 
    print("The weather is hot.")
"""
Ask the user to enter vsome words and names.
"""

names = list(input("Please enter names or words and seperate them using ,: "))
newlist = sorted([name for name in names if name.startswith("a" or "A") and len(name) > 3])
with open("names.txt", "w", encoding = "utf-8") as file:
    for name in newlist:
        file.write(name + "\n")
print(f"File saved successfully with {len(newlist)} names.")

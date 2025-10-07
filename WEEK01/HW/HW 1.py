text = str(input("Write a sentence, or simply your name: "))
no_space = text.replace(" ", "")
vowels = "aeiouAEIOU"

result = ""
for v in no_space:
    if v in vowels:
        result = result + "."
    else:
        result = result + v

reversed = "".join(reversed(result))
print(reversed)
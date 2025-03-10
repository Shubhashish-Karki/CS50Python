#making a list of vowels
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

#prompt for user to input
string = input("Input: ")

for s in string:
    if s not in vowels:
        print(s, end="")

print()
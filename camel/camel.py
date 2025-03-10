#prompt the user for input
case = input("camelCase: ")

#use a loop to find uppercase character and change with snakecase
for c in case:
    if c.isupper():
        print("_", c.lower(), sep ="", end = "") #sep to separate _ and character with nothing and end to ensure no new line
    else:
        print(c, end = "")

print() # to print a new line after printing in snake case
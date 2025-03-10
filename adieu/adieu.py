import inflect

p = inflect.engine()
# declaring a list
names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    else:
        # method to include item in a list
        names.append(name)

print("Adieu, adieu, to " + p.join(names))

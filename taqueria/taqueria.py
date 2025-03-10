menu ={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
#defining total cost to 0
total = 0
#prompt the user till user hits control-d
while True:
    try:
        item = input("Item: ").title()
        menu[item]    #to raise key error if not exist
    except EOFError: # if user hits control d while input
        break
    except KeyError:   # if key does not exist in dictionary
        pass
    else:
        if item in menu:
            total += menu[item]
        print(f"Total: ${total:.2f}")

print()
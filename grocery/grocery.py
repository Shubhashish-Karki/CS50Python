#declaring a dictionary for grocery items
grocery_item = {}

while True:
    try:
        item = input().upper()
    #for end of input control d
    except EOFError:
        print()
        break
    else:
        #to check if key exists in grocery or not, if yes increase value by 1
        if item in grocery_item:
            grocery_item[item] += 1
        else:
            grocery_item[item] = 1

#copying the keys of dict to list for sorting
list = grocery_item.keys()

for item in sorted(list) :
    print(grocery_item[item], item)
#prompt the input for greetings

greeting = input("Greeting: ").lstrip().capitalize()

#checking for hello

if greeting.find("Hello", 0, 5) != -1:      #find() returns -1 if substring not found between string[0:5]
    print("$0")

elif greeting.find("H" , 0) != -1:
    print("$20")

else:
    print("$100")


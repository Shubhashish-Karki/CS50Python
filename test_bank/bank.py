def main():
    greeting = input("Greeting: ").lstrip()
    print(f"${value(greeting)}")

def value(greeting):
    greeting = greeting.capitalize()
    if greeting.find("Hello", 0, 5) != -1:      #find() returns -1 if substring not found between string[0:5]
        return 0

    elif greeting.find("H" , 0) != -1:
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()



#a main function to prompt the user and to output meal time
def main():
    time = input("What time it is? ")
    meal = convert(time)

    if 7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print("lunch time")
    elif 18 <= meal <= 19:
        print("dinner time")

#to split the time and return the hour and minute time
def convert(time):
    hr, min = time.split(":")
    return round((float(hr) + float(min) / 60 ), 2)

if __name__ == "__main__":
    main()
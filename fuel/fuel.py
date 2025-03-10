while True:
    fuel  = input("Fraction: ")
    try:
        x, y = fuel.split("/")
        guage = int(x) / int(y) * 100
        if int(x) > int(y):
            continue
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break


if guage <= 1:
    print("E")
elif guage >= 99:
    print("F")
else:
    print(f"{guage:.0f}%")
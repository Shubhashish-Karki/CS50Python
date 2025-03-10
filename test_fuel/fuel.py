import sys

def main():
    fuel = input("Fraction: ")
    print(gauge(convert(fuel)))

def convert(fraction):
    try:
        x, y = fraction.split("/")
        percentage = int(x) / int(y) * 100
        if int(x) > int(y):
            raise ValueError
    except ValueError:
        raise
    except ZeroDivisionError:
        raise
    except TypeError:
        taise
    else:
        return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return(f"{percentage:.0f}%")


if __name__ == "__main__":
    main()

import sys
from datetime import date
import inflect
import math


def main():
    print(convert(input("Date of Birth: ").strip()))


def convert(birth_date):
    p = inflect.engine()
    # checking for correct format
    try:
        date.fromisoformat(birth_date)
    except:
        sys.exit("Invalid")
    # splitting given date into year month and day
    year, month, day = birth_date.split("-")
    # difference of todays and given time
    time = date.today() - date(int(year), int(month), int(day))
    # first calculating in seconds, converting to minutes and then converting into words
    words = p.number_to_words(math.trunc(time.total_seconds() / 60), andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()

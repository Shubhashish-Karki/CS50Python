# Defining a list of months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").strip()
        # if given in 12/3/1992 format
        if date.find("/") != -1:
            month, day, year = date.split("/")
        # if given in September 8, 1992 format
        # Here i have used index to raise a value error if both first and second condition dont meet
        # I couldnot use index in first condition because it would raise a value error and loop again
        elif date.index(",") != -1:
            date = date.replace(",", "")
            month, day, year = date.split(" ")
            if month in months:
                month = (months.index(month) + 1)
        #Check for correct value of month and day
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            break
        else:
            continue

    except ValueError:
         pass

print(f"{year}-{int(month):02}-{int(day):02}")


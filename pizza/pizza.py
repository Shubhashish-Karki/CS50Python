import sys
import csv
from tabulate import tabulate

pizza = []

# check for no of arguments

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
# check if .csv file or not
elif sys.argv[1].find(".csv") == -1:
    sys.exit("Not a CSV file")

try:
    file_name = sys.argv[1]
    with open(f"{file_name}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if file_name == "regular.csv":
                pizza.append(
                    {
                        "Regular Pizza": row["Regular Pizza"],
                        "Small": row["Small"],
                        "Large": row["Large"],
                    }
                )
            #for sicilian file
            else:
                pizza.append(
                    {
                        "Sicilian Pizza": row["Sicilian Pizza"],
                        "Small": row["Small"],
                        "Large": row["Large"],
                    }
                )
except FileNotFoundError:
    sys.exit("File does not exist")

# Using the keys as header for title column
print(tabulate(pizza, headers="keys", tablefmt="grid"))

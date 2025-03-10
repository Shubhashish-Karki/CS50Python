import sys
import csv

# check for no of arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    # saving file names
    file_input = sys.argv[1]
    file_output = sys.argv[2]

    # reading from input file
    with open(f"{file_input}") as file:
        reader = csv.DictReader(file)
        # writing to a file
        with open(f"{file_output}", "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            # to give title column name from field names
            writer.writeheader()
            # storing the second splitted item (,) of first column for every row in first name and first splitted item in last name
            for row in reader:
                writer.writerow(
                    {
                        "first": row["name"].split(",")[1].lstrip(),
                        "last": row["name"].split(",")[0],
                        "house": row["house"],
                    }
                )

except FileNotFoundError:
    sys.exit(f"Could not read {file_input}")

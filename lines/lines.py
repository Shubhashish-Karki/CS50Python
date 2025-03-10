import sys

# check for no of arguments
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
# check if file is not valid
elif sys.argv[1].find(".py") == -1:
    sys.exit("Not a Python file")

count = 0

try:
    file_name = sys.argv[1]
    with open(f"{file_name}") as file:
        lines = file.readlines()
    for line in lines:
        # for any indentation it is necessary to strip spaces
        if line.lstrip().startswith("#") or line.isspace():
            continue  # do nothing
        else:
            count += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(f"{count}")

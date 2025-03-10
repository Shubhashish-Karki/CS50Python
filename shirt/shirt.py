import sys
import os.path
from PIL import Image, ImageOps

# creating a list exe to include extension available
exe = ["jpg", "jpeg", "png"]

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) == 3:
    # path.split returns path and file name which is then splitted at .
    name_1, ext_1 = os.path.split(sys.argv[1])[1].lower().split(".")
    name_2, ext_2 = os.path.split(sys.argv[2])[1].lower().split(".")
    if ext_1 not in exe:
        sys.exit("Invalid input")
    elif ext_2 not in exe:
        sys.exit("Invalid output")
    elif ext_1 != ext_2:
        sys.exit("Input and output have different extensions")
    else:
        try:
            shirt = Image.open("shirt.png")
            # getting the size of the shirt
            size = shirt.size
            with Image.open(sys.argv[1]) as input:
                # the input picture is matched with size of the shirt
                input = ImageOps.fit(input, size)
                # pasting the shirt over input, second arg shirt represents mask indicating pixels to be updated
                input.paste(shirt, shirt)
                # saving the updated photo with output file name
                input.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")

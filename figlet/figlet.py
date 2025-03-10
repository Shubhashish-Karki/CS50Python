from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

available = figlet.getFonts()

# To output random font
if len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=random.choice(available))
    print(figlet.renderText(text))
# To ensure correct format
elif len(sys.argv) == 3 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    if sys.argv[2] in available:
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    # To exit if not available font
    else:
        sys.exit("Invalid usage")
# To exit if any of the option dont match
else:
    sys.exit("Invalid usage")

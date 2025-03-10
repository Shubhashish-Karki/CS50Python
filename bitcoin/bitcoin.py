import requests
import sys

#check for no arguments
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    # assign the no of bitcoin
    bitcoin = float(sys.argv[1])
    # copying the response of request
    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # if arg not a number
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit()
else:
    # converting response in a json format
    res = req.json()
    # here bpi is a dictionary with USD as nested dictionary
    rate = res["bpi"]["USD"]["rate_float"]
    print(f"${bitcoin * rate:,.4f}")


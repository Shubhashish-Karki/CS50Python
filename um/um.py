import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r"\bum\b", s, re.I):   #I == IGNORECASE
        count = 0
        # find all returns list of all matched pattersns
        for _ in matches:
            count = count + 1
        return count
    else:
        return 0


if __name__ == "__main__":
    main()

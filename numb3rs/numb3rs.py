import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    # using walrus (:=) to assign to matches and check if it is empty or not
    if matches := re.search(
        r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip
    ):  # \d is a decimal digit and + means repeating it once or more
        for group in matches.groups():
            # for every group resulting in a tuple converting to integer and comapring
            if int(group) <= 255:
                pass
            else:
                return False
        return True
    # if match is none
    else:
        return False


if __name__ == "__main__":
    main()

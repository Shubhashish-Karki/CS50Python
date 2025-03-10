import random


def main():
    l = get_level()
    score = 0
    # generating 10 random questions
    for _ in range(10):
        x = generate_integer(l)
        y = generate_integer(l)
        # giving 3 trials
        for _ in range(3):
            try:
                ans = int(input(f"{x} + {y} = "))
                # if correct add 1 to score
                if ans == x + y:
                    score += 1
                    break
                else:
                    # if not correct
                    print("EEE")
                    continue
            # if input is else than numbers
            except ValueError:
                pass
        # if 3 trials answer is wrong
        if ans != x + y:
            print(f"{x} + {y} = {x + y}")
    # after leaving initial loop show score
    print(f"Score: {score}")


def get_level():
    # level can only be 1,2 or 3
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            # checking for level in list named levels
            if level not in levels:
                raise ValueError
        except ValueError:
            pass
        else:
            return level


def generate_integer(level):
    if level == 1:
        # return 1 digit number
        return random.randrange(0, 10)
    elif level == 2:
        # return 2 digit number
        return random.randrange(10, 100)
    else:
        # return 3 digit number
        return random.randrange(100, 1000)


if __name__ == "__main__":
    main()

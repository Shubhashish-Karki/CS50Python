import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1 or level > 100:
            continue
    except ValueError:
        pass
    else:
        break
# randrange will return a random integer from a to n - 1
guess = random.randrange(1, level + 1)

while True:
    try:
        ans = int(input("Guess: "))
        if ans < 1 or ans > 100:
            continue
    except:
        pass
    else:
        if ans > guess:
            print("Too large!")
            continue
        elif ans < guess:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break

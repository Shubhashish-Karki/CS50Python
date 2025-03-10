import emoji

text = input("Input: ")
emojis = text.split()

for e in emojis:
    #checking for strings that are convertable to emoji
    if ":" in e:
        print(emoji.emojize(f"{e} ", language="alias"), end="")
    else:
        print(f"{e} ", end="")

print()

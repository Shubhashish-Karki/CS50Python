vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]


def main():
    word = input("word: ")
    print(shorten(word))


def shorten(word):
    string = ""
    for s in word:
        if s not in vowels:
            string += s
    return f"{string}"


if __name__ == "__main__":
    main()

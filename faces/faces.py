# Convert function
def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


#main function
def main():
    text = input("Input your text: ")
    print(convert(text))

main()

#prompt the user

ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? " ).strip().lower()

#print based on answer

if ans == "42" or ans == "forty-two" or ans == "forty two":
    print("Yes")
else:
    print("No")
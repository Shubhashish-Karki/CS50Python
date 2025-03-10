def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #check for length if max or min not satisfy then
    if len(s) < 2 or len(s) > 6:
        return False
    #if first two is not a letter
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False
     #if string is consists of period,space or punctuation
    elif s.isalnum() == False:
        return False
    else:
        #i start from 2 as s[0] and s[1] cant be numeric at all
        i = 2
        while i < len(s):
            #check if first number is 0
            if s[i].isnumeric() and s[i] == "0":
                return False
            #if first number is not 0 then check if remaining are also numeric then return true or false
            elif s[i].isnumeric():
                return (s[i + 1:].isnumeric())
            i += 1
        #returns true if length is less than 2
        return True
    
main()
#defining denomination list
denomination = [25, 10, 5]

#total due amount
due = 50

#while loop to ask till due becomes cleared
while due != 0:
    print("Amount Due:", due)
    cents = int(input("Insert Coin: "))
    #checking if inserted amount in denomination or not
    if cents in denomination:
        due -= cents
        #break if the total payamount becomes greater than 50
        if due < 0:
            break
    else:
        continue

#if any owes left
print("Change Owed:", -due)
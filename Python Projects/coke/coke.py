def main():
    amountDue = 50
    print("Amount Due: ", amountDue)
    amount = int(input("Insert Coin: "))
    calculation(amount, amountDue)

def calculation(amount, amountDue):
    while amountDue > 0:
        if amount == 25 or amount == 10 or amount == 5:
            amountDue -= amount
            if amountDue > 0:
                print("Amount Due:", amountDue)
                amount = int(input("Insert Coin: "))
            elif amountDue == 0 or amountDue < 0:
                print("Change Owed:", amountDue * -1)
        else:
            print("Amount Due:", amountDue)
            break

main()


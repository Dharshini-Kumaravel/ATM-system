print("--ATM system--")
balance=1000
while True:
    print("Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if(choice==1):
        print("Your balance is:",balance)
    elif(choice==2):
        amount=int(input("Enter the amount to deposit: "))
        balance+=amount
        print("Your new balance is:",balance)
    elif(choice==3):
        amount=int(input("Enter the amount to withdraw: "))
        if(amount>balance):
            print("Insufficient balance!")
        else:
            balance-=amount
            print("Your new balance is:",balance)
    elif(choice==4):
        print("Thank you for using the ATM system!")
        break
    else:
        print("Invalid choice!")

balance=500
print(f"---------------Welcome to ATM simulation---------------\npress 1 for withdraw money\npress 2 for deposite money\npress 3 for checkng balance")
while True:
    a=int(input(f"enter your choice: "))
    if a==1:
        amount=int(input(f"Enter the amount you want to withdraw: "))
        if amount<=balance:
            print(f"{amount}Rs withdrawn.your balance is {balance-amount}")
        else:
            print(f"insufficient balance.your balance is {balance}")
    elif a==2:
        amount=int(input(f"Enter the amount you want to deposite: "))
        balance+=amount
        print(f"{amount}Rs added.your balance is {balance}")
    elif a==3:
        print(f"your balance is {balance}")
    else:
        print("invalid input")
    choice=input(f"press 'u' to use again and press 'e' to exit atm: ")  
    if choice=="e"or choice=="E":
        print("---------------thank you for using atm---------------")
        break     
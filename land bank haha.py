


def withdraw(balance,amount):
    return balance -amount

def deposit(balance,amount):
    return balance +amount

balance = 1000
while True:
    print("1. balance")
    print("2. withdrAW")
    print("3. deposit")

    choice = int(input("picknumber :"))

    if choice== 1:
        print(f"my balance:{balance}")
    elif choice ==2:
        amount = int(input("how much: "))
        balance = withdraw(balance,amount)
        print(f"Transaction Successfully balance:-{amount}")
    elif choice == 3:
        amount = int(input("how much: "))
        balance = deposit(balance,amount)
        print(f"Transaction Successfully balance:+{amount}")

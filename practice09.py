def show_menu():
    print("-------Menu------")
    print("1. BALANCE NI KO'RISH ")
    print("2. PUL KIRITISH  ")
    print("3. PUL YECHISH  ")
    print("0. CHIQISH  ")

def deposit(balance, amount):
    if amount > 0:
        balance += amount
    return balance 

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount

    return balance

def chesk_balance(balance):
    print(f"sizning balansingiz: {balance}")

def main():
    balance = 100.000

    while True:
        show_menu()

        op = input(">")
        if op == "1":
            chesk_balance(balance)
        elif op =="2":
            amount = float(input("Amount:"))
            balance = deposit(balance,amount)
        elif op == "3":
            amount = float(input("Amount:"))
            balance = withdraw(balance,amount)
        elif op == "0":
            break
        else:
            print("bunday menu yo'q")

main()
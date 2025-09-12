from rich.console import Console
from rich.prompt import Prompt

console = Console()


def show_menu():
    console.print("-------Menu------" , style = "bold red")
    console.print("1. BALANCE NI KO'RISH ", style="italic bright_blue")
    console.print("2. PUL KIRITISH  ",style="bold green")
    console.print("3. PUL YECHISH  ",style="italic blue" )
    console.print("0. CHIQISH  ",style="underline bright_green" )

def deposit(balance, amount):
    if amount > 0:
        balance += amount
    return balance 

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount

    return balance

def chesk_balance(balance):
    console.print(f"sizning balansingiz: {balance}",style = "blue")

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
            console.print("bunday menu yo'q", style = "red")

main()
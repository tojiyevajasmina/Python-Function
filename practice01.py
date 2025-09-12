from rich.console import Console
from rich.prompt import Prompt

console = Console()


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return 

def main():
    while True:
        num1 = int(Prompt.ask ("[magenta] 1-son:"))
        num2 = int(Prompt.ask("[magenta] 2-son:"))
        ch = Prompt.ask("[cyan] Amal:")

        
        if ch == "+":
            result = add(num1, num2 )
        elif ch == "-":
            result = subtract(num1 ,num2)
        elif ch == "*":
            result = multiply(num1, num2)
        elif ch == "/":
            result = divide(num1, num2)

        print(  result)

main()
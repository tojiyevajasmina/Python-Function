from rich.console import Console
from rich.prompt import Prompt

console = Console()


def calculate_tax(salary):
    tax_percent = 0
    if salary > 5000000:
        tax_percent = 20  
    else:
        tax_percent = 13  
    
    tax = salary * tax_percent / 100

    return tax

def calculate_net_salary(salary):
    net_salary = salary - calculate_tax(salary)

    return net_salary

maosh = float(input("Maoshingizni kiriting: "))

soliq = calculate_tax(maosh)
s= calculate_net_salary(maosh)

console.print(f"Soliq miqdori: {soliq} so'm",style = "magenta")
console.print(f"Sof maosh: {s} so'm", style =  "blue")
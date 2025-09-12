from rich.console import Console
from rich.prompt import Prompt

console = Console()

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    return bmi


def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    

weight = float(Prompt.ask("[bold green]Og'irligingizni kiriting (kg)[/]"))
height = float(Prompt.ask("[bold blue]Bo'yingizni kiriting (metr)[/]"))



bmi = calculate_bmi(weight, height)

status = bmi_status(bmi)


console.print(f"BMI: {bmi}",style = "yellow")
console.print(f"Holat: {status}",style = "blue")

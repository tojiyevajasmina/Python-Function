from rich.console import Console
from rich.prompt import Prompt

console = Console()


def c_to_f(celsius):
    return celsius * 9/5 + 32

# Fahrenheit dan Celsius ga o‘tkazish
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    tanlov = Prompt.ask("[italic yellow]Tanlang (1: C → F, 2: F → C, 0: Chiqish)[/italic yellow]")


    
    if tanlov == "1":
        c = float(input("Celsius kiriting: "))
        console.print("Fahrenheit:", c_to_f(c), "F", style = "red")
    elif tanlov == "2":
        f = float(input("Fahrenheit kiriting: "))
        console.print("Celsius:", f_to_c(f), "C", style = "green")
    elif tanlov == "0":
        console.print("Dastur yakunlandi.", style = "cyan")
        break
    else:
        console.print("Noto'g'ri tanlov, qayta urinib ko'ring." ,style = "magenta")
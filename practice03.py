from rich.console import Console
from rich.prompt import Prompt

console = Console()


def is_even(number):
    return number % 2 == 0

# Natijani chiqaramz
def print_even_message(number):
    if is_even(number):
        console.print(f"{number} — juft son" , style ="magenta")
    else:
        console.print(f"{number} — toq son", style = "red")

# Foydalanuvchidan son olish va natijani chiqaramz
son = int(Prompt.ask("[underline yellow]Son kiriting: [/]"))
print_even_message(son)
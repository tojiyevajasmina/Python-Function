from rich.console import Console
from rich.prompt import Prompt

from datetime import date

console = Console()

def calculate_age(birth_year):
    current_date = date.today()


    age = current_date.year - birth_year
    return age

name = Prompt.ask("[green] NAME:")


birth_year = int(Prompt.ask("[magenta] Birth year:"))

age = calculate_age(birth_year)
console.print(f"{name} ,sizning yoshingiz: {age} da", style = "yellow")
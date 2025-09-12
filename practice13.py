from rich.console import Console
from rich.prompt import Prompt

console = Console()


def is_palindrome(text):
    return text == text[::-1]


soz = Prompt.ask("[bold red] So'z kiriting: ")

if is_palindrome(soz):
    console.print("Bu so'z palindrom ",style = "italic yellow")
else:
    console.print("Bu so'z palindrom emas ", style = "italic green")

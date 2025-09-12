from rich.console import Console
from rich.prompt import Prompt

console = Console()


secret_number = 7

def check_guess(secret, guess):
    result=  secret == guess
    return result


def print_result(is_correct):
    if is_correct:
        console.print("To'g'ri!", style = "green")
    else:
        console.print("Xato!" ,style = "red" )



guess = int(Prompt.ask("[yellow] Sirli sonni toping: "))

result = check_guess(secret_number, guess)
print_result(result)
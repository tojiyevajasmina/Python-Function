from rich.console import Console
from rich.prompt import Prompt

console = Console()


def is_valid_phone_number(phone):
    result =  phone.isdigit() and len(phone) == 9

    return result
    
attemps = 0
while True:
    phone = Prompt.ask("[yellow]Telefon raqamni kiriting:")
    attemps += 1
    if is_valid_phone_number(phone):
        console.print("Telefon raqam to'g'ri.",style = "green")
        break
    else:
        console.print("Xato!  qayta urinib ko'ring." , style = "red")
        continue    



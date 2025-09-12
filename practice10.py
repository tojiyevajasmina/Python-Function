from rich.console import Console
from rich.prompt import Prompt

console = Console()


def is_strong_password(password):
    
    checked = len(password) >= 8 
    if checked:
        return checked
    
def main():

    
    while True:

        password = input( "Parol kiriting:: ")
        checked = is_strong_password(password)
        if checked:
            console.print(" KUCHLI parol !" , style = "green ")
            break
        else:
            console.print(" KUCHSIZ parol qayta urinib ko`ring! " , style = "red")


main()

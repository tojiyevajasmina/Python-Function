from rich.console import Console
from rich.prompt import Prompt

console = Console()



def ask_question(question , correct_answer):

    console.print (question,style ="red")  
    entered = input("> ") 

    if check_answer(entered,correct_answer):
        console.print("to'g'ri ", style =" yellow")
    else:
        console.print("noto'g'ri", style ="green ")

def check_answer(user_answer, correct_answer):
    result = user_answer.lower() == correct_answer.lower()
    
    return result
    
def quiz():
    ask_question("Uzbekiston poytaxti?" ,  "Toshkent")


quiz()
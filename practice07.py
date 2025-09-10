questions = "O`zbekiston nechanchi yil mushtaqil bo'lgan?"

correct_answer = "1991"

print(questions)

print("Variantlar: \n1992 ta \n1991 ta \n1990 ta \n1993 ta")

user_answer = input("> ")

def check_answer(user_answer, correct_answer):
    
    if user_answer == "1991":
        print("Tog`ri topdingiz! ")
    
    else:
        print("Noto`g`ri javob!! ")

check_answer(user_answer, correct_answer)

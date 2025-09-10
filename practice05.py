def check_guess(secret, guess):
    return secret == guess

def print_result(is_correct):
    if is_correct:
        print("To'g'ri!")
    else:
        print("Xato!")


secret_number = 7

user_guess = int(input("Sirli sonni toping (1 dan 10 gacha): "))

# Tekshiramiz va natijani chiqaramiz
result = check_guess(secret_number, user_guess)
print(result)
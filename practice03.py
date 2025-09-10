def is_even(number):
    return number % 2 == 0

# Natijani chiqaramz
def print_even_message(number):
    if is_even(number):
        print(f"{number} — juft son.")
    else:
        print(f"{number} — toq son.")

# Foydalanuvchidan son olish va natijani chiqaramz
son = int(input(" son kiriting: "))
print_even_message(son)
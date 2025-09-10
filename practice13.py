def is_palindrome(text):
    return text == text[::-1]


soz = input("So'z kiriting: ")

if is_palindrome(soz):
    print("Bu so'z palindrom ")
else:
    print("Bu so'z palindrom emas ")

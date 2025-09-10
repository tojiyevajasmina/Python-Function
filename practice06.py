def is_valid_phone_number(phone: str):
    if phone.isdigit() and len(phone) == 9:
        return True
    else:
        return False
while True:
    phone = input("Telefon raqamni kiriting (faqat 9 ta raqam): ")
    if is_valid_phone_number(phone):
        print("Telefon raqam to'g'ri.")
        break
    else:
        print(" Xato!  qayta urinib ko'ring.")    



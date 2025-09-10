def is_strong_password(password):
    
    checked = len(password) >= 8 
    if checked:
        return checked
    
def main():

    
    while True:

        password = input("Parol kiriting:: ")
        checked = is_strong_password(password)
        if checked:
            print(" KUCHLI parol ! ")
            break
        else:
            print(" KUCHSIZ parol qayta urinib ko`ring! ")


main()

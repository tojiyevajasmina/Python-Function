
def c_to_f(celsius):
    return celsius * 9/5 + 32

# Fahrenheit dan Celsius ga o‘tkazish
def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    tanlov = input("Tanlang (1: C → F, 2: F → C, 0: Chiqish): ")
    
    if tanlov == "1":
        c = float(input("Celsius kiriting: "))
        print("Fahrenheit:", c_to_f(c), "F")
    elif tanlov == "2":
        f = float(input("Fahrenheit kiriting: "))
        print("Celsius:", f_to_c(f), "C")
    elif tanlov == "0":
        print("Dastur yakunlandi.")
        break
    else:
        print("Noto'g'ri tanlov, qayta urinib ko'ring.")
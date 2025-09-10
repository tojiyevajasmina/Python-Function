def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
    
def multiply(a, b):
    return a * b
    
def divide(a, b):
    return 

def main():
    while True:
        num1 = int(input("1-son:"))
        num2 = int(input("2-son:"))
        ch = input("Amal:")

        
        if ch == "+":
            result = add(num1, num2 )
        elif ch == "-":
            result = subtract(num1 ,num2)
        elif ch == "*":
            result = multiply(num1, num2)
        elif ch == "/":
            result = divide(num1, num2)

        print(result)

main()
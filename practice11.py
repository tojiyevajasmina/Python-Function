def calculate_tax(salary):
    if salary > 5000000:
        tax_rate = 0.20  
    else:
        tax_rate = 0.13  
    
    tax = salary * tax_rate
    return tax

def calculate_net_salary(salary):
    tax = calculate_tax(salary)
    net_salary = salary - tax
    return net_salary

maosh = float(input("Maoshingizni kiriting: "))

soliq = calculate_tax(maosh)
s= calculate_net_salary(maosh)

print(f"Soliq miqdori: {soliq} so'm")
print(f"Sof maosh: {s} so'm")
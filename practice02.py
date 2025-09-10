from datetime import date

def calculate_age(birth_year):
    current_date = date.today()

    age = current_date.year - birth_year
    return age

birth_year = int(input("birth year:"))

age = calculate_age(birth_year)
print(f"sizning yoshingiz: {age}")
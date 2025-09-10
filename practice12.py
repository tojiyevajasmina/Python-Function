def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    

weight = float(input("Og'irligingizni kiriting (kg): "))
height = float(input("Bo'yingizni kiriting (metr): "))


bmi = calculate_bmi(weight, height)

status = bmi_status(bmi)


print(f"BMI: {bmi}")
print(f"Holat: {status}")

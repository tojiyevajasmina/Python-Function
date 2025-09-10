
def get_grade(score):
    grade = "" 
    if 90 <= score <= 100:
        grade = "A"
    elif 80 <= score <= 89:
        grade = "B"
    elif 70 <= score <= 79:
        grade = "C"
    elif 60 <= score <= 69:
        grade = "E"
    elif 0 <= score <= 59:
        grade = "F"

    return grade

ball = int(input("ball: "))
grade = get_grade(ball)
print(grade)
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    grade = grade_calculator(score)
    print(grade)


def grade_calculator(score):
    if score < 0 or score > 100:
        grade = ("Invalid score")
    elif score > 90:
        grade = ("Excellent")
    elif score > 50:
        grade = ("Passable")
    else:
        grade = ("Bad")
    return grade


main()

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science


students = [
    Student("정수아", 87, 98, 88, 95),
    Student("손이안", 92, 98, 96, 98),
    Student("정슬기", 100, 96, 94, 90)
]

print(students[0].name)
print(students[0].korean)
print(students[0].math)

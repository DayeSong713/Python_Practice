class Student:
    def __init_(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )


students = [
    Student("정수아", 87, 98, 88, 95),
    Student("손이안", 93, 88, 77, 98),
    Student("정슬기", 100, 96, 94, 90)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))

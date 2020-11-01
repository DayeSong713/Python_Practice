import math


class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum()/4

    def to_string(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_avg()
        )


students = [
    Student("송다예", 95, 100, 97, 99),
    Student("손이안", 92, 98, 96, 98),
    Student("정슬기", 100, 96, 94, 90)
]

print("이름", "총점", "평균", sep="\t")

for st in students:
    print(st.to_string())


class Student:
    def __init__(self):
        pass

    def study(self):
        print("study hard")


class Teacher:
    def teach(self):
        print("teach student")


classroom = [Student(), Student(), Teacher(), Student(), Student()]


#student = Student()

#print("isinstance(student, Student):", isinstance(student, Student))


for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()


class Student:
    def __init__(self, name, korean, math, english, science):
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
        return "{}\t{}\t{}\t".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )


students = [
    Student("송다예", 99, 100, 100, 100),
    Student("손이안", 92, 98, 96, 98,),
    Student("정슬기", 100, 96, 94, 90)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))


class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))


students = [
    Student("송다예", 99, 100, 100, 100),
    Student("손이안", 92, 98, 96, 98,),
    Student("정슬기", 96, 96, 94, 90)
]

print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))


class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------ 학생 목록 ------")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("------ ------ ------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum()/4

    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(),
                                   self.get_average())


Student("송다예", 99, 100, 100, 100)
Student("손이안", 92, 98, 96, 98,)
Student("정슬기", 96, 96, 94, 90)

Student.print()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2*math.pi*self.radius

    def get_area(self):
        return math.pi*(self.radius**2)


circle = Circle(-3)
print("원의 둘레 : ", circle.get_circumference())
print("원의 널이 : ", circle.get_area())


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2*math.pi*self.__radius

    def get_area(self):
        return math.pi*(self.__radius**2)


circle = Circle(-3)
print("원의 둘레 : ", circle.get_circumference())
print("원의 널이 : ", circle.get_area())

print(circle.__radius)


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_circumference(self):
        return 2*math.pi*self.__radius

    def get_area(self):
        return math.pi*(self.__radius**2)

    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        if(value <= 0):
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value


circle = Circle(1)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())
print()

print(circle.get_radius())

circle.set_radius(-2)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())


class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__메서드가 호출되었습니다.")

    def test(self):
        print("Parent 클래스의 test() 메서드입니다.")


class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__메서드가 호출되었습니다.")


child = Child()
child.test()
# print(child.value)

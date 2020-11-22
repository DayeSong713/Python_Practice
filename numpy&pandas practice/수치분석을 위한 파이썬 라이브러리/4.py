def hi():
    print("hello")


print(hi())


def hi2(x):
    print(x)


print(hi2('ddd'))


class Person:
    def __init__(self, name):
        self.name = name
        print("call")

    def hello(self):
        print("hello"+self.name)

    def goodbye(self):
        print("goodbye" + self.name)


p1 = Person("Daye")
p1.hello()
p1.goodbye()

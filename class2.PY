'''
class Person:
    def greeting(self):
        print("안녕하세요")


j = Person()

j.greeting()


class Person2:
    def __init__(self):
        self.hello = "hi"

    def greeting(self):
        print(self.hello)


j2 = Person2()
j2.greeting()

'''


class Per:
    def __init__(self, name, age, address):
        self.hello = "안녕"
        self.name = name
        self.age = age
        self.address = address

    def gre(self):
        print("{}저는 {}입니다.".format(self.hello, self.name))


me = Per("송다예", "27", "서울시")
me.gre()

print(me.name)
print(me.age)
print(me.address)

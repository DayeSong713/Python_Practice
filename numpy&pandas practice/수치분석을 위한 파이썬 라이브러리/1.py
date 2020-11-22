k = 'kim'
l = 'lee'

kl = '%s %s' % (k, l)
print(kl)

str = 'good'

print(str.upper())

str = 'hello'

print(str.rjust(9))
print(str.center(9))


print(str.replace('e', '^'))

str2 = '  hello  '
print(str2.strip())

print(str2.count('l'))

print(str2.find(' '))
print(str2.find('l'))

aa = [1, 2, 3, 4]
aa.pop()
print(aa)

aa.append(True)
print(aa)

number = range(10)
print(number)

print(number[6])

number = [1, 2, 3, 4, 5]

print(number[2:3])

print(number[2:5])

print(number[:2])

print(number[1:])

print(number[-2])

animals = ['dog', 'cat', 'monkey']
print(animals)

for animal in animals:
    print(animal)


num = [1, 2, 3, 4, 5]
square = []
for i in num:
    square.append(i**2)
print(square)


square2 = [i**2 for i in num]
print(square2)

num2 = [2, 4, 6, 8]
square3 = [x**2 for x in num2]
print(square3)

num3 = [0, 1, 2, 3, 4, 5]

odd_square = [x**2 for x in num3 if x % 2 == 1]
print(odd_square)

even_square = [x**2 for x in num3 if x % 2 == 0]
print(even_square)

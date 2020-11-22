from math import sqrt
animals = {'dog', 'cat'}

print('dog' in animals)

animals.add('lion')

print(animals)

print(len(animals))

animals.add('dog')
print(animals)

animals.add(1)
print(animals)

animals.remove('cat')
print(animals)

for animal in animals:
    print(animal)


numb = {int(sqrt(x)) for x in range(30)}
print(numb)

d = {(a, a+1): a for a in range(10)}

print(d)

t = (2, 3)

print(d[t])

print(d[5, 6])

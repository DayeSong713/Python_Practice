dic = {'cat': 'cute', 'dog': 'furry'}

print(dic['cat'])

print(dic['dog'])

print('cat' in dic)

d = {'a': 'aa'}

print(d)

d2 = {'a': '', 'b': 'bb', 'c': 'cc'}

print('a' in d2)

print('d' in d2)

print(d2['a'])

d2['a'] = 'aaa'
print(d2)

del d2['a']
print(d2)
print('a' in d2)

d2['a'] = 'aa'
print(d2)

print(d2.get('d', 'null'))
print(d2.get('a', 'null'))

d = {'person': 10, 'cat': 5, 'dog': 3}

for animal in d:
    num = d[animal]
    print('%s is %d' % (animal, num))

for animal, number in d.items():
    print('%s is %s' % (animal, number))

num = [0, 1, 2, 3, 4]
even_s = {x: x**2 for x in num if x % 2 == 0}
print(even_s)

from random import randint
a = input('Enter word: ')
b = input('Enter word: ')
x = len(a)
y = len(b)
z = randint(0, x)
c = randint(0, y)
print(a[0 : z] + b[c :])


f = open('123.txt', 'r')
suma = 0
n = 0
for i in f:
    g = int(i[len(i) - 2])
    suma += g
    n += 1
    if g < 3:
        print(i[:-1])
print('Средний балл: %.2f' % (suma/n))
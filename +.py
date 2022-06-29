#Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.

import random
n = 5
m = 5

a = [[0]* m for i in range(n)]

for i in range(n):
    for j in range(m):
        a[i][j] = random.randint(1,100)

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='')
    print()

max = 0
id = 0
i = 0
for key in a:
    if sum(key) > max:
        max = sum(key)
        id = i
    i += 1
print(id, '-', max)







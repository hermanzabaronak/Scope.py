import random
a = [random.randint(0, 5) for i in range(5)]
b = tuple(a)
c = [random.randint(-5,0) for i in range (5)]
d = tuple(c)
e = b + d
print(b)
print(d)
print(e)
print("Количество нулей", e.count(0))
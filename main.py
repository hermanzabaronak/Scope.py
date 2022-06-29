import random

a = [random.randint(1,10) for i in range(10) ]
b = tuple(a)
print(b)
print("max" max(a), "min" min(a))
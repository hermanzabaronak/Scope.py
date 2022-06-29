print(" Hi there! This is my first calculator.\n If you want to add press 1.\n If you want to subtract press 2.\n If you want to multiple press 3.\n If you want to divide press 4.")

def add(a,b):
    return a + b
def sub(a,b):
     return a - b
def mult(a,b):
    return a * b
def devd(a,b):
    return a / b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input('Chose the action: '))
if c == 1:
    print(add(a,b))
elif c == 2:
    print(sub(a,b))
elif c == 3:

    print(mult(a,b))

elif c == 4:
    print(devd(a,b))
else:
    print("Error")

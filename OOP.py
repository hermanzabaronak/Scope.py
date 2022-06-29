class calculator:
    def __init__(self):
        self.func4()
    def func(self):
        return self.a + self.b
    def func1(self):
        return self.a - self.b
    def func2(self):
        return self.a * self.b
    def func3(self):
        if self.b == 0:
            return 'error'
        else:
            return self.a / self.b
    def func4(self):
        self.a = int(input())
        self.b = int(input())
while True:
    print('+, -, *, /')
    x = input()
    print('Numbers: ')
    example = calculator()
    if x == "6":
        break
    if x == "+":
        print(example.func)
    if x == "-":
        print(example.func1)
    if x == "/":
        print(example.func2())
    if x == "/":
        print(example.func3())



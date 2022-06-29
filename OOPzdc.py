class Human:
    default_name = "Name"
    default_age = 0
    def __init__(self, name=default_name, age=default_age):
        #Dynamic fields
        self.name = name
        self.age = age
        #Private
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')
    @staticmethod
    def default_info():
        print(f'Default Name: {Human.default_name}')
        print(f'Default Age: {Human.default_age}')
    def earn_money(self, amount):
        print(f'Earned {amount} money! Current value: {self.__money}')



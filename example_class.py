class TheHouse():
    def __init__(self, color, size):
        self.color = color
        self.size = size
    def location(self):
        print((self.color.title() + "is fancy"))
    def price(self):
        print((self.size() + "is affordable"))
my_house = TheHouse('black', 120)
print("My house is "+ my_house.color + ".")
print("My house's size is "+ str(my_house.size) +'.')
u_house = TheHouse('green', 60)

print('Your house has a ' + u_house.color + ' color.')
print('Your house size is ' + str(u_house.size) + '.')

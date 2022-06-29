print('We have 3 burgers:\n - Gamburger\n - Cheeseburger\n - Krabsburger\n Which one do you order?')

def burger_make(discription, wiegth, *burgers):
    for burger in burgers:
        print('- ' + burger)
a = input("Enter the burger: ")
if a == gamburger:
    print(burger_make('Meat', 300, Gamburger))
elif a == cheeseburger:
    print(burger_make("Cheese", 250, Cheeseburger))
elif a == krabsburger:
    print(burger_make('Crab', 270, Crabsburger))


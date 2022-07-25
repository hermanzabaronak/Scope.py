import random
a = random.randint(1,10)
b = random.randint(1,2)
i = 0
while i < 5:
    i+=1
    g = int(input("Enter the number: "))
    g1 = int(input("Enter the color: "))
    if g > a:
        print ("Incorrect")
    elif g == a and b == g1:
        print ("You win!")
        break
    else:
        print("Not yet")
else:
    print("You lost :(")
    
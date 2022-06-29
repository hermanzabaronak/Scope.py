enter = input("Enter your credit card: ")
def card_h(card):
    return '*' * (len(card)-4) + card[-4:]
print(card_h(enter))
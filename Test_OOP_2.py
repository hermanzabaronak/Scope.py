enter = input("Enter the sentence: ")
def Palindrome(string):
    abc = str(string)
    if abc[::-1].startswith(abc):
        return True
    else:
        return False
print(Palindrome(enter))
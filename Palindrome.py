#------------Program to check if string is a palindrome or not--------------------

user = input("Enter a word: ").lower()
if user == user[::-1]:
    print("This word is a palindrome")
else:
    print("This is not a palindrome")




#-----------------------------SORTING WORDS------------------------

user = input("Enter a sentence: ").lower()
x = user.split()
x= sorted(x)
y = sorted(x,reverse = True)

print(x)
print("This has been sorted in reverse " + str(y))



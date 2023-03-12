x = input()
x2 = reversed(x)
y = "".join(x2)

if x == y:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
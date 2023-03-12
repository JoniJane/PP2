x = input()
u = l = 0

for i in x:
    if 123>ord(i)>96:
        l = l+1
    elif 91>ord(i)>64:
        u = u+1

print("the number of upper case letters: ",u )
print("the number of lower case letters: ",l)
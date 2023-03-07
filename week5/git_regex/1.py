import re
#file = open('row.txt', 'r')
#file = open('https://github.com/arnee99/Spring-PP2/blob/main/Lab5/row.txt', 'r')
a = input()
print(re.findall(r".*a.*b{0}",a))
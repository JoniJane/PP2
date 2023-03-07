import re

a = input()  
x = re.findall("[A-Z][a-z]+", a)
print(x) 
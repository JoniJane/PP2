import re

a = input()
#print(re.split("[A-Z]", a))
print(re.findall("[A-Z][^A-Z]*", a))
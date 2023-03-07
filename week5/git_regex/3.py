import re

a = input()  
x = re.search(".*[a-z]+_[a-z]", a)
print(x.string) 
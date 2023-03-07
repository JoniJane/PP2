import re
a = input()

print(re.findall(".*a.*b$", a))
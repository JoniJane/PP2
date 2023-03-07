import re

a = input()
print(re.findall(r".*a.*b{2,3}",a))
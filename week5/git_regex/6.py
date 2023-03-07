import re
a = input()
print(re.sub("[.| |,]", ":", a))
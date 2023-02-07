s = input()
for x in range(len(s)):
    if x % 3 == 0:
        s = s.replace(s[x], '3', 1)
print(s.replace('3', ''))
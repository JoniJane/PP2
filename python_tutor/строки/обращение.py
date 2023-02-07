s = str(input())
x = s[:s.find('h')]
y = s[s.find('h'):s.rfind('h')+1]
z = s[s.rfind('h')+1:]
print(x + y[::-1] + z)
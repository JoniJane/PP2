s = str(input())
t = s[s.find('h')+1:s.rfind('h')]
print(s[:s.find('h')+1] + t.replace('h', 'H') + s[s.rfind('h'):])
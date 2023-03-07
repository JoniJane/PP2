import re 

def f(a):
    return a.group("g1")+ " " + a.group("g2")

x = input()
g = "(?P<g1>[a-z])(?P<g2>[A-Z])"

print(re.sub(g, f, x))
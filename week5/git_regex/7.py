import re

def f(a):
    return a.group("g1") + a.group("g3").upper()

x = input()
g = "(?P<g1>[a-z])(?P<g2>[_])(?P<g3>[a-z])"

print(re.sub(g, f, x))
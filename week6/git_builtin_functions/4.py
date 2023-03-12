from math import sqrt as s
import time

x = int(input())
y = int(input())

time.sleep(y/1000)
ans = float(s(x))

print(f"Square root of {x} after {y} miliseconds is {ans}")
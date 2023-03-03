import datetime as d
x = d.datetime.now()
y = x - d.timedelta(1)
z = x +  d.timedelta(1)

print("Yesterday was", y.strftime("%A"))
print("Today is", x.strftime("%A"))
print("Tomorrow will be", z.strftime("%A"))
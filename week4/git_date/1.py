import datetime as d
x = d.datetime.now()
y = x - d.timedelta(5)

print("Today is", x.strftime("%A"))
print("5 days ago was", y.strftime("%A"))
import datetime as d

x = input()
y = input()

x = d.datetime.strptime(x, "%Y.%m.%d.%H.%M.%S")
y = d.datetime.strptime(y, "%Y.%m.%d.%H.%M.%S")

if x>y: 
    diff=x-y 
else: 
    diff=y-x 

print("the difference in seconds is ", diff.total_seconds())


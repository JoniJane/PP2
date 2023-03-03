import json
x = '{"name": "Janelle", "age":17, "city": "Almaty"}'
y = json.loads(x)
print(y["age"])
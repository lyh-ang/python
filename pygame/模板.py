import json

with open('045.json') as json_f:
    number = json.load(json_f)

print(str(number))


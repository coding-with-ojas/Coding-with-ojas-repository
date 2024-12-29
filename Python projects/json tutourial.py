import json

with open('file.json', 'w') as file:
    json.dump('Hello my name is ojas', file)

with open('file.json', 'r') as file:
    data = json.load(file)
    print(data)

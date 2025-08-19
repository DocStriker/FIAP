import json

with open('dados_exemplo.json', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)
    print(data)
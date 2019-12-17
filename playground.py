import json

json_content = None

with open('info.json') as file_reference:
    json_content = json.load(file_reference)


for item in json_content:
    print(
        f'Item after serialization: {json.dumps(item, indent=4)}')
    print('------------------------------------')

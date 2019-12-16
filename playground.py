import json

data_tuple = ('Mercury', 'Venus', 'Earth', 'Mars')
data_list = ['Jupiter', 'Saturn', 'Uranus', 'Neptune']
data_dict = {"star": "Sun", "galaxy": 'Milky Way'}

# convert collections to json string
json_tuple = json.dumps(data_tuple)
json_list = json.dumps(data_list)
json_dict = json.dumps(data_dict)

print(f'json_tuple: {json_tuple}')
print(f'json_list: {json_list}')
print(f'json_dict: {json_dict}')

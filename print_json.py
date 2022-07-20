import json

with open('test_file.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)

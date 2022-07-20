import json

# печать всего JSON-объекта:
with open('test_file.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)

# печать части JSON-объекта:
json_str = json.loads(json_data)
print(json_str["blog"])

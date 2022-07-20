import json

# печать всего JSON-объекта:
with open('test_file.json', 'r') as j:
    json_data = json.load(j)
    json_data_str = json.dumps(json_data, indent=4)
    print(json_data_str)

# печать части JSON-объекта:
print(json_data["blog"])

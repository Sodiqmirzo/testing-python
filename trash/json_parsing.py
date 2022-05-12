import json

atring_as_json_format = '{"name": "John", "age": 30}'
obj = json.loads(atring_as_json_format)

key = "name"

if key in obj:
    print(obj[key])
else:
    print(f"{key} not found")

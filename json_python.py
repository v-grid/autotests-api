import json

"""json_data = '{"a":1, "b":2, "c":3, "name": "Alex", "age": 22, "is_student": false }'

json_str = json.dumps(json_data)
parsed_json = json.loads(json_data)
print(json_str, type(json_str))
print(parsed_json, type(parsed_json))
"""

"""data = {
    'name': 'Alex',
    'age': 22,
    'is_student': True
}
json_str = json.dumps(data, indent=4)
parsed_json = json.loads(json_str)
print(json_str, type(json_str))"""

with open("json_exemple.json", "r", encoding = "utf-8") as file:
    data = json.load(file)
    print(data)

with open ("json_users.json", "w", encoding = "utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

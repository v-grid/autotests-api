import json

json_data = '{ "name": "Иван", "age": "30", "is_student" : "true"}'
parset_data = json.loads(json_data)

print(parset_data)
json_string = json.dumps(parset_data, indent=4)

print(json_string)
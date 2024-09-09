import json

json_data='{"id":1,"name": "Aish"}'
data=json.loads(json_data)
#1st way
print("id:", data['id'])
#2nd way to print
print(data['id'])
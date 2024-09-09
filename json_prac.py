import json

json_data='{"id":1,"name": "Aish"}'
data=json.loads(json_data)
print("id:", data['id'])
import json
data = {"name":"francis","age":22, "nacionalidad":"chiricano"}

with open ('data.json', 'w') as file:
 	json.dump(data,file)
	
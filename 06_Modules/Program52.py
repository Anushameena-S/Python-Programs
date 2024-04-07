#JSON Module

import json

data ={"Name":"Ace","Shares":100,"Price":540}
json_str=json.dumps(data)
print("Json data is :",json_str)
print("Json Data Type is :", type(json_str))

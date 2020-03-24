import json
#做两个版本的,只是接口变化而已
f=open("JSON_DATA\\001.json")
js=json.loads(f.read())
print(js)
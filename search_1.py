import json

data=open("JSON_DATA",encoding="utf-8")
dJson=json.loads(data.read())
data.close()

key=input()
for i in dJson[key]:
    print()

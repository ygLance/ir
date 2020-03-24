import json
with open("001.json") as f:
    tmp=json.loads(f.read())
    print(tmp[","])
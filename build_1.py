#只有分词的 丐版
import div.div_main
import os
import json


walkTmp=os.walk("data")
filenames=[j for i in walkTmp for j in i[2]]
filenames_num=len(filenames)

with open("JSON_DATA\\filenames.json",mode="w") as f_tmp:
    f_tmp.write(json.dumps(filenames))

fJson=open("JSON_DATA\\001.json",mode="w",encoding= "utf-8")#清空json
sJson={}

for i in range(filenames_num):
    rus_div=div.div_main.en_div(filenames[i])# 应该去掉符号
    for word in rus_div:
        if word not in sJson:
            sJson[word]=[i]
        else :
            if sJson[word][-1]!=i :
                sJson[word].append(i)

rJson=json.dumps(sJson,indent=4)
fJson.write(rJson)
fJson.close()
import jieba
import nltk
import re

Path=r"data"

DOCID={}
walkTmp=os.walk(Path)

for i in walkTmp:#i是一个tuple
    for j in i[2]:#j是文件名
        with open("data\\" + Path) as f1:
            ans = re.split(r"[．.？?!！]", f1.read())
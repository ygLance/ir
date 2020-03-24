import jieba
import nltk
import re
#  算了,直接全读进去算了

def en_div(Path):##TODO 去除标点
    #TODO 处理全角
    with open("data\\"+Path) as f1:
        sentences=re.split(r"[．.？?!！]",f1.read())# 分句结果

    ans=[]
    for i in sentences:
        tokens=nltk.word_tokenize(i)
        ans.extend(tokens)
    return ans
def ch_div():

    ...
if __name__ == '__main__':
    Path="Some.txt"
    with open(Path) as d:
        print(d.read(10))

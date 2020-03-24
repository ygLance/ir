import div.div_main
import os

walkTmp=os.walk("data")
for i in walkTmp:#i是一个tuple
    for j in i[2]:#j是文件名
        div.div_main.div_ch(j)#只传文件名,目录自己写
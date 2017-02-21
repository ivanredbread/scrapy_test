import json
import re
import pandas as pd
import numpy as np


f = open("bangumi.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
data = json.load(f)
f.close()

link   = []
name   = []
num    = []
score  = []
youleng= []
info   = []

for i in range(len(data)):
    value  = float(data[i]['score'][0])**(np.e/2)/float(re.findall(r"\d+\.?\d*",data[i]['num'][0])[0])*1000
#    if float(data[i]['score'][0]) >= 7.0:
    if value >= 100.0 and float(data[i]['score'][0]) >= 7.0:
        link.append(data[i]['link'][0])
        name.append(data[i]['name'][0])
        num.append(data[i]['num'][0])
        score.append(data[i]['score'][0])
        youleng.append(format(value,'.2f'))
        info.append(re.sub(r'\s+','', data[i]['info'][0]))

index  = np.int64(np.linspace(1,len(youleng),len(youleng)))
df = pd.DataFrame(np.array([link,name,num,score,youleng,info]).T,\
                  index=index,columns=['link','名字','评分数','得分','优冷指数','信息'])
df['得分']   = df['得分'].astype(float)
df['优冷指数'] = df['优冷指数'].astype(float)
df = df.sort(['优冷指数'],ascending=False)
df = df.reset_index(drop=True)
del df['link']

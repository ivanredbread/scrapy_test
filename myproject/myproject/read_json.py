import json
import re
import pandas as pd
import numpy as np
import mysql.connector
import sys
from mysql.connector import errorcode


#================================ read json ===================================
with open("bangumi.json", encoding='utf-8') as f:  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    data = json.load(f)

link   = []
name   = []
num    = []
score  = []
youleng= []
info   = []

for i in range(len(data)):
    value  = float(data[i]['score'][0])**(np.e/2)/float(re.findall(r"\d+\.?\d*",data[i]['num'][0])[0])*1000
    number = float(re.findall(r"\d+\.?\d*",data[i]['num'][0])[0])
#    if float(data[i]['score'][0]) >= 7.0:
    if  float(data[i]['score'][0]) <= 6.0 and number >= 1000.0:
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
df = df.sort_values(['优冷指数'],ascending=False)
df = df.reset_index(drop=True)
del df['link']
#============================== insert to mysql ===============================
user = 'root'
pwd  = '19910805'
host = '127.0.0.1'
db   = 'test'
  
create_table_sql = "CREATE TABLE IF NOT EXISTS mytable ( \
                    id int(10) AUTO_INCREMENT PRIMARY KEY, \
		    name varchar(20), score float(4) ) \
		    CHARACTER SET utf8"
    
insert_sql = "INSERT INTO mytable(name, score) VALUES ('Jay', 22 ), ('杰', 26)"
select_sql = "SELECT id, name, score FROM mytable"

cnx = mysql.connector.connect(user=user, password=pwd, host=host)
cursor = cnx.cursor()
      

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cnx.database = db  
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        cnx.database = db
    else:
        print(err)
        exit(1)
        

#try:
#    cursor.execute(create_table_sql)
#except mysql.connector.Error as err:
#    print("create table 'mytable' failed.")
#    print("Error: {}".format(err.msg))
#    sys.exit()
#    
#try:
#    cursor.execute(insert_sql)
#except mysql.connector.Error as err:
#    print("insert table 'mytable' failed.")
#    print("Error: {}".format(err.msg))
#    sys.exit()
# 
# 
#for i in range(len(df)):
#    sql = "INSERT INTO mytable (name, score) VALUES ('{}', {})".format(df["名字"][i],df["得分"][i])
#    try:
#        cursor.execute(sql)
#    except mysql.connector.Error as err:
#        print("insert table 'mytable' from file 'bangumi.json' -- failed.")
#        print("Error: {}".format(err.msg))
#        sys.exit()
 
try:
    cursor.execute(select_sql)
    for (id, name, age) in cursor:
        print("ID:{}  Name:{}  Score:{}".format(id, name, score))
except mysql.connector.Error as err:
    print("query table 'mytable' failed.")
    print("Error: {}".format(err.msg))
    sys.exit()
 
cnx.commit()
cursor.close()
cnx.close()
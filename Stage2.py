#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 20:23:02 2020

@author: xor
"""
import pandas as pd 
#file=pd.read_json('data.json')

"""
li=[]
data=[]
col=[]
kk=[]
dtype=[]
command=[]
for i in file.items():
    li.append(i)
for i in range(len(li)):
    col.append(li[i][0])
for i in range(1,len(li[0][1]),1):
    kk=[]
    for j in range(57):
        kk.append([col[j],li[j][1][i]])
    data.append(kk)
for i in kk:
    dtype.append(type(i[1])) 
    
for i in range(len(dtype)):
    if dtype[i]==str:
        dtype[i]='text'
    elif dtype[i]==dict:
        dtype[i]='JSONB'
    elif dtype[i]==numpy.float64:
        dtype[i]='float'
    elif dtype[i]==numpy.int64:
        dtype[i]='int'
        
#creating insert command generic 
for i in range(len(col)):
    cmd+=col[i]+" "+dtype[i]+',' #cmd for creating the table
#creating the table
cur.execute("CREATE TABLE DATA("+cmd[:-1]+")")
#making command to insert data
for k in data:
    insert_cmd=''
    for i in k:
        if i!=k[-10]:
            insert_cmd+="'"+str(i[1])+"'"+","
        else:
            insert_cmd+='##'
    try:
        i1=insert_cmd.split('##')
        q=json.dumps(k[-10][1])
        command.append([i1[0][:-1],q,i1[1][:-1]])
    except:
        pass
#entring the data into table
for i in range(len(command)):
    cur.execute("INSERT INTO DATA VALUES("+command[i][0]+",'"+command[i][1]+"',"+command[i][2]+")")
    print(i/len(command))
    """

import psycopg2
con = psycopg2.connect(database="postgres", user="xor", password="", host="127.0.0.1", port="5432")
cur = con.cursor()

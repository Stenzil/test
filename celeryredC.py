#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 15:18:26 2020

@author: xor
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:22:16 2019

for doc in records.aggregate([
    { "$match": {
        "latitude": { "$gte": 20, "$lte": 20.15 }
    }}
]):
    print(doc)

record=db.so.find_one({"geo":{
                        "coordinates" :[28.65,77.2164]})

db.so.create_index([("geo","2dsphere")])

 db.so.find({"geo": {
    "$near": {
        "$geometry": {
            "type": "Point" ,
            "coordinates": [ 60, 22 ]
        },
        "$maxDistance": 80000
    }
}}).count()
    
    db.so.insert_one({
    "geo" : {
        "type" : "Point",
        "coordinates" : [ 
            61.1111, 
            23.111123
        ]
    }
})

@author: xor
"""
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import json
from starlette.requests import Request
from pymongo import MongoClient
from celery import Celery
from celery.result import AsyncResult

from main import *
request= Request
file=pd.read_csv('IN.csv')
k=file.values.tolist()
cli=MongoClient('mongodb+srv://stenzil:pandey@cluster0-6cu9y.mongodb.net/test?retryWrites=true&w=majority')
db=cli.get_database('TASK')
records=db.somedata
reco=db.org
col=file.columns
class post_LAT(BaseModel):
    key : str
    place_name : str
    admin_name1 : str
    latitude : float
    longitude: float
    accuracy : float
    
class LAT(BaseModel):
    longitude: float
    latitude: float
class final(BaseModel):
    lo: float
    lan: float

app = FastAPI()

@app.get("/ge")
def ge(fin: final):
    k=gp.delay(fin.lo,fin.lan)
    """
    
    res = AsyncResult(str(k),app=app)
    res.status # will return the status of the request 
    res.get() #will return the output which could be matched later
    
    """
    return str(k)

@app.get("/get_l")
def get_l(fin: final):
    k=gl.delay(fin.lo,fin.lan)

    return str(k)

@app.get("/get_location/")
async def get_location(lat: LAT):
    record=db.so.find_one(
{	"geo" : {
		"type" : "Point",
		"coordinates" : [lat.latitude,lat.longitude]
	}})
    del record['_id']
    del record['accuracy']
    del record['geo']
    print(record)
    return record
    
@app.post("/post_location/")
async def post_location(push: post_LAT):
    a={}
    record=db.so.find_one({"key":push.key})
    if record==None: 
        a[col[0]]=push.key
        a[col[1]]=push.place_name
        a[col[2]]=push.admin_name1
        a["geo"] = {
               "type" : "Point",
               "coordinates" : [ 
                   push.latitude, 
                   push.longitude
               ]
        }
        a[col[5]]=push.accuracy
        db.so.insert_one(a)
        return 'Added'
    else:
        return 'Already Exists'
@app.get("/get_using_postgres/")
async def get_using_postgres(lat: LAT):
    record=db.so.find({"geo": {
    "$near": {
        "$geometry": {
            "type": "Point" ,
            "coordinates": [ lat.latitude, lat.longitude ]
        },
        "$maxDistance": 5000
    }
}})
    key=[]
    for i in record:
        key.append(i['key'])
    return key
@app.get("/pl/")
async def pl():
    q=gp.delay(77.2167)
    return q
    

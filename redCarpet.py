#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 19:22:16 2019

@author: stenzil
"""

from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import json
from starlette.requests import Request
from pymongo import MongoClient


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


app = FastAPI()

 

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
async def get_using_postres(lat: LAT):
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 16:42:35 2020

@author: xor
"""

from celery import Celery 
app = Celery('redC', broker='redis://localhost:6379/0',backend="amqp://")
from pydantic import BaseModel
import json
from starlette.requests import Request
from pymongo import MongoClient

request= Request

cli=MongoClient('mongodb+srv://stenzil:pandey@cluster0-6cu9y.mongodb.net/test?retryWrites=true&w=majority')
db=cli.get_database('TASK')
records=db.somedata
reco=db.org

class LAT(BaseModel):
    longitude: float
    latitude: float


@app.task
def getit(s):
    return s[0]
@app.task
def get_spots(o):
    return o[-1]
@app.task
def gq(lat,long):
    return 'bhak'

@app.task(queue='high')
def gp(a,b):
    record=db.so.find({"geo": {
    "$near": {
        "$geometry": {
            "type": "Point" ,
            "coordinates": [ a, b ]
        },
        "$maxDistance": 5000
    }
}})
    key=[]
    for i in record:
        key.append(i['key'])
    return key
@app.task()
def gl(a,b):
    record=db.so.find_one(
{	"geo" : {
		"type" : "Point",
		"coordinates" : [a,b]
	}})
    del record['_id']
    del record['accuracy']
    del record['geo']
    print(record)
    return record


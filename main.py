#! /usr/bin/python

import json
import urllib2
import time
import boto3

URI = 'https://hub.docker.com/v2/repositories/rgee0/'
TABLE_NAME = 'dockerStats'
FIELDS = ['pull_count', 'star_count']

if(__name__=="__main__"):

    dynamodb = boto3.resource('dynamodb')
    timeOfRequest = int(time.time())

    table = dynamodb.Table(TABLE_NAME)
    data = urllib2.urlopen(URI)
    json = json.load(data)

    for record in json['results']:
        output = {}
        output['timestamp'] = timeOfRequest
        output['name'] = record['namespace'] + "\\" + record['name'] 
        for field in FIELDS:
            output[field] = record[field]
        response = table.put_item(Item=output)


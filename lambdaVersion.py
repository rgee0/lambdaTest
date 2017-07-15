import json
import urllib2
import time
import boto3

def lambda_handler(event, context):

    URI = 'https://hub.docker.com/v2/repositories/rgee0/'
    TABLE_NAME = 'dockerStats'
    FIELDS = ['pull_count', 'star_count']
    
    dynamodb = boto3.resource('dynamodb')
    timeOfRequest = int(time.time())
    
    table = dynamodb.Table(TABLE_NAME)
    data = json.load(urllib2.urlopen(URI))
    
    for record in data['results']:
        output = {}
        output['timestamp'] = timeOfRequest
        output['name'] = record['namespace'] + "\\" + record['name'] 
        for field in FIELDS:
            output[field] = record[field]
        table.put_item(Item=output)
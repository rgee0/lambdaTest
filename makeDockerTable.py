#! /usr/bin/python

import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table(  
    TableName='dockerStats',
    KeySchema=[
        {
            'AttributeName': 'name', 
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'timestamp', 
            'KeyType': 'RANGE'
        }
    ], 
    AttributeDefinitions=[
        {
            'AttributeName': 'timestamp', 
            'AttributeType': 'N'
        }, 
        {
            'AttributeName': 'name', 
            'AttributeType': 'S'
        }, 
    ], 
    ProvisionedThroughput={
        'ReadCapacityUnits': 1, 
        'WriteCapacityUnits': 1
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='dockerStats')  
print(table.item_count)  
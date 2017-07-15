#! /usr/bin/python

import boto3

dynamodb = boto3.resource('dynamodb')  
table = dynamodb.Table('dockerStats')

table.delete() 
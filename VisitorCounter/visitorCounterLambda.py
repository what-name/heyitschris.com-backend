### NOTES
# Created by Chris Nagy on 15.05.2020

# Create an IAM Role for this Lambda function with the following:
# DynamoDB allow: getItem, updateItem
# or maybe if the retrieval and update will be two seperate Lambda functions
# then put the two roles for updateItem and getItem seperately on the two functions
# probably going to keep it in one Lambda function tho for simplicity
#
# Increment an atomic counter in DynamoDB
# Link:
# https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.03.html#GettingStarted.Python.03.03
#
# TO-DO: put this on a blog post incl. frontend js code
### END NOTES

import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
ddbTableName = os.environ['databaseName']
table = dynamodb.Table(ddbTableName)

def handler(event, context):
    ddbResponse = table.update_item(
        Key={
            "id": "visitorCount"
        },
        UpdateExpression='ADD amount :inc',
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues="UPDATED_NEW"
    )
    print("Response visitor count: ", ddbResponse["Attributes"]["amount"])
    responseBody = json.dumps({"visitorCount": int(float(ddbResponse["Attributes"]["amount"]))})
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody,
        "headers": {
            "Access-Control-Allow-Headers" : "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,OPTIONS" 
        },
    }
    return apiResponse
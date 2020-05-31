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

# Define environment variables
table_env_variable = os.environ['table']

# Define resource for DynamoDB
dynamodb = boto3.resource('dynamodb')
# Define table
# Make sure to define the environment variable in your Lambda function
# The execution will fail if not. You can also edit the code to hardcode your table
table = dynamodb.Table(table_env_variable)

def lambda_handler(event, context):
    # Update the item
    response = table.update_item(
        # Find the item based on the Primary Key
        Key={
            "id": "visitorCount"
        },
        # "Set" update expression
        UpdateExpression='SET amount = amount + :inc',
        # Define the attribute values
        ExpressionAttributeValues={
            ':inc': 1
        },
        # Return values - no idea what this means lol
        ReturnValues="UPDATED_NEW"
    )
    # Print the result for safe measure, can be commented out in prod
    print("Response visitor count: ", response["Attributes"]["amount"])
    # Return visitor count from response object
    return {
        "statusCode": 200,
        "visitorCount": response["Attributes"]["amount"]
    }
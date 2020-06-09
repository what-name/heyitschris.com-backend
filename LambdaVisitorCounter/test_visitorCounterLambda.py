### Unit test for the visitorCounterLambda function

#from visitorCounterLambda import handler
import boto3
import os
from moto import mock_dynamodb2


def aws_credentials():
    # """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@mock_dynamodb2
def test_handler():
  from visitorCounterLambda import handler
  # Database table name into env variable
  os.environ['databaseName'] = 'heyitschris'

  dynamodb = boto3.client('dynamodb')
  ddbTableName = os.environ['databaseName']
  
  # Create mock table
  dynamodb.create_table(
    TableName = ddbTableName,
    BillingMode='PAY_PER_REQUEST',
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ]
  )
  
  # Put required item into mock table
  dynamodb.put_item(
    TableName=ddbTableName,
    Item={
      'id': {'S':'visitorCount'},
      'amount': {'N':'1'}
    }
  )

  # Get item for testing
  item = dynamodb.get_item(
    TableName=ddbTableName,
    Key={
      'id': {'S':'visitorCount'}
    }
  )
  print("Item in Mock Table: ", item["Item"])

  handler(0, 0)
 
  # Print out all the tables for testing
  # tablesListed = dynamodb.list_tables()
  # print(tablesListed)



if __name__ == '__main__':
  aws_credentials()
  test_handler()
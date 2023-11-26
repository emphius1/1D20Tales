```python
import boto3
from boto3.dynamodb.conditions import Key, Attr

# AWS credentials
AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_SECRET_KEY'
AWS_REGION = 'YOUR_REGION'

# DynamoDB client
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id=AWS_ACCESS_KEY,
                          aws_secret_access_key=AWS_SECRET_KEY,
                          region_name=AWS_REGION)

# DynamoDB tables
characters_table = dynamodb.Table('Characters')
inventory_table = dynamodb.Table('Inventory')
game_states_table = dynamodb.Table('GameStates')

def create_table(table_name):
    """
    Function to create a DynamoDB table
    """
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
        print(f"Table {table_name} created successfully.")
    except Exception as e:
        print(f"Error creating table {table_name}.")
        print(e)

# Create tables
create_table('Characters')
create_table('Inventory')
create_table('GameStates')
```
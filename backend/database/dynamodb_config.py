```python
import boto3
from botocore.exceptions import NoCredentialsError

def create_dynamodb_client():
    try:
        dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
        return dynamodb
    except NoCredentialsError:
        print("No AWS credentials found.")
        return None

def create_tables(dynamodb):
    if dynamodb is None:
        return

    # Create characters table
    characters_table = dynamodb.create_table(
        TableName='Characters',
        KeySchema=[
            {
                'AttributeName': 'character_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'character_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Create inventory table
    inventory_table = dynamodb.create_table(
        TableName='Inventory',
        KeySchema=[
            {
                'AttributeName': 'item_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'item_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Create game states table
    game_states_table = dynamodb.create_table(
        TableName='GameStates',
        KeySchema=[
            {
                'AttributeName': 'state_id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'state_id',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print("Tables created successfully.")

dynamodb = create_dynamodb_client()
create_tables(dynamodb)
```
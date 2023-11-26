```python
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('characters')

def create_character(character):
    response = table.put_item(Item=character)
    return response

def get_character(character_id):
    response = table.get_item(Key={'character_id': character_id})
    return response['Item']

def update_character(character_id, updates):
    response = table.update_item(
        Key={'character_id': character_id},
        AttributeUpdates=updates
    )
    return response

def delete_character(character_id):
    response = table.delete_item(Key={'character_id': character_id})
    return response
```
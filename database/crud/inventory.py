```python
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')

def create_item(character_id, item):
    table.put_item(
        Item={
            'character_id': character_id,
            'item_id': item['item_id'],
            'item_name': item['item_name'],
            'item_type': item['item_type'],
            'item_description': item['item_description'],
            'item_stats': item['item_stats']
        }
    )

def get_item(character_id, item_id):
    response = table.get_item(
        Key={
            'character_id': character_id,
            'item_id': item_id
        }
    )
    return response['Item']

def update_item(character_id, item_id, new_item):
    table.update_item(
        Key={
            'character_id': character_id,
            'item_id': item_id
        },
        UpdateExpression="set item_name=:n, item_type=:t, item_description=:d, item_stats=:s",
        ExpressionAttributeValues={
            ':n': new_item['item_name'],
            ':t': new_item['item_type'],
            ':d': new_item['item_description'],
            ':s': new_item['item_stats']
        },
        ReturnValues="UPDATED_NEW"
    )

def delete_item(character_id, item_id):
    table.delete_item(
        Key={
            'character_id': character_id,
            'item_id': item_id
        }
    )

def get_character_inventory(character_id):
    response = table.query(
        KeyConditionExpression=Key('character_id').eq(character_id)
    )
    return response['Items']
```
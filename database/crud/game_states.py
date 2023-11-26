```python
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('game_states')

def create_game_state(character_id, game_state):
    response = table.put_item(
        Item={
            'character_id': character_id,
            'game_state': game_state
        }
    )
    return response

def get_game_state(character_id):
    response = table.get_item(
        Key={
            'character_id': character_id
        }
    )
    return response['Item']

def update_game_state(character_id, game_state):
    response = table.update_item(
        Key={
            'character_id': character_id
        },
        UpdateExpression="set game_state=:s",
        ExpressionAttributeValues={
            ':s': game_state
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

def delete_game_state(character_id):
    response = table.delete_item(
        Key={
            'character_id': character_id
        }
    )
    return response
```
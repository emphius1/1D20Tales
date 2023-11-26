```python
import boto3
from boto3.dynamodb.conditions import Key
from dynamodb_config import dynamodb

def create_character(table_name, character):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=character)
    return response

def get_character(table_name, character_id):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={'character_id': character_id})
    return response['Item']

def update_character(table_name, character_id, updates):
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key={'character_id': character_id},
        AttributeUpdates=updates
    )
    return response

def delete_character(table_name, character_id):
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key={'character_id': character_id})
    return response

def create_inventory(table_name, inventory):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=inventory)
    return response

def get_inventory(table_name, inventory_id):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={'inventory_id': inventory_id})
    return response['Item']

def update_inventory(table_name, inventory_id, updates):
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key={'inventory_id': inventory_id},
        AttributeUpdates=updates
    )
    return response

def delete_inventory(table_name, inventory_id):
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key={'inventory_id': inventory_id})
    return response

def create_game_state(table_name, game_state):
    table = dynamodb.Table(table_name)
    response = table.put_item(Item=game_state)
    return response

def get_game_state(table_name, game_state_id):
    table = dynamodb.Table(table_name)
    response = table.get_item(Key={'game_state_id': game_state_id})
    return response['Item']

def update_game_state(table_name, game_state_id, updates):
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key={'game_state_id': game_state_id},
        AttributeUpdates=updates
    )
    return response

def delete_game_state(table_name, game_state_id):
    table = dynamodb.Table(table_name)
    response = table.delete_item(Key={'game_state_id': game_state_id})
    return response
```
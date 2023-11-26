```python
from flask import Blueprint, request, jsonify
from database.crud.characters import create_character, get_character, update_character, delete_character

characters = Blueprint('characters', __name__)

@characters.route('/characters', methods=['POST'])
def create():
    data = request.get_json()
    response = create_character(data)
    return jsonify(response)

@characters.route('/characters/<character_id>', methods=['GET'])
def retrieve(character_id):
    response = get_character(character_id)
    return jsonify(response)

@characters.route('/characters/<character_id>', methods=['PUT'])
def update(character_id):
    data = request.get_json()
    response = update_character(character_id, data)
    return jsonify(response)

@characters.route('/characters/<character_id>', methods=['DELETE'])
def delete(character_id):
    response = delete_character(character_id)
    return jsonify(response)
```
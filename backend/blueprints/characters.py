```python
from flask import Blueprint, request, jsonify
from backend.character_creation.base_stats import calculate_base_stats
from backend.character_creation.traits_abilities import select_traits_abilities
from backend.character_creation.appearance import customize_appearance
from backend.database.crud_operations import create_character, get_character, update_character, delete_character

characters = Blueprint('characters', __name__)

@characters.route('/characters', methods=['POST'])
def create():
    data = request.get_json()
    base_stats = calculate_base_stats(data['race'], data['class'])
    traits_abilities = select_traits_abilities(data['race'], data['class'])
    appearance = customize_appearance(data['appearance'])
    character = create_character(data['name'], base_stats, traits_abilities, appearance)
    return jsonify(character), 201

@characters.route('/characters/<character_id>', methods=['GET'])
def retrieve(character_id):
    character = get_character(character_id)
    if character:
        return jsonify(character), 200
    else:
        return jsonify({'error': 'Character not found'}), 404

@characters.route('/characters/<character_id>', methods=['PUT'])
def update(character_id):
    data = request.get_json()
    updated_character = update_character(character_id, data)
    if updated_character:
        return jsonify(updated_character), 200
    else:
        return jsonify({'error': 'Character not found'}), 404

@characters.route('/characters/<character_id>', methods=['DELETE'])
def delete(character_id):
    deleted_character = delete_character(character_id)
    if deleted_character:
        return jsonify({'message': 'Character deleted'}), 200
    else:
        return jsonify({'error': 'Character not found'}), 404
```
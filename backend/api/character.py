```python
from flask import Blueprint, request, jsonify
from backend.database.crud_operations import create_character, get_character, update_character, delete_character

character_bp = Blueprint('character_bp', __name__)

@character_bp.route('/character', methods=['POST'])
def create():
    data = request.get_json()
    response = create_character(data)
    return jsonify(response), 201

@character_bp.route('/character/<character_id>', methods=['GET'])
def retrieve(character_id):
    response = get_character(character_id)
    if response:
        return jsonify(response), 200
    else:
        return jsonify({"error": "Character not found"}), 404

@character_bp.route('/character/<character_id>', methods=['PUT'])
def update(character_id):
    data = request.get_json()
    response = update_character(character_id, data)
    if response:
        return jsonify(response), 200
    else:
        return jsonify({"error": "Character not found"}), 404

@character_bp.route('/character/<character_id>', methods=['DELETE'])
def delete(character_id):
    response = delete_character(character_id)
    if response:
        return jsonify({"message": "Character deleted"}), 200
    else:
        return jsonify({"error": "Character not found"}), 404
```
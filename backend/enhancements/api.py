```python
from flask import Blueprint, request, jsonify
from backend.api.character import CharacterAPI
from backend.api.inventory import InventoryAPI

api_enhancements = Blueprint('api_enhancements', __name__)

class EnhancedCharacterAPI(CharacterAPI):
    def get(self, character_id):
        character = super().get(character_id)
        # Add enhancements here
        return character

    def put(self, character_id):
        character = super().put(character_id)
        # Add enhancements here
        return character

class EnhancedInventoryAPI(InventoryAPI):
    def get(self, inventory_id):
        inventory = super().get(inventory_id)
        # Add enhancements here
        return inventory

    def put(self, inventory_id):
        inventory = super().put(inventory_id)
        # Add enhancements here
        return inventory

@api_enhancements.route('/characters/<int:character_id>', methods=['GET', 'PUT'])
def enhanced_character(character_id):
    api = EnhancedCharacterAPI()
    if request.method == 'GET':
        return jsonify(api.get(character_id))
    elif request.method == 'PUT':
        return jsonify(api.put(character_id))

@api_enhancements.route('/inventory/<int:inventory_id>', methods=['GET', 'PUT'])
def enhanced_inventory(inventory_id):
    api = EnhancedInventoryAPI()
    if request.method == 'GET':
        return jsonify(api.get(inventory_id))
    elif request.method == 'PUT':
        return jsonify(api.put(inventory_id))
```
```python
from flask import Blueprint, request
from database.crud.inventory import get_inventory, add_item, remove_item

inventory_bp = Blueprint('inventory_bp', __name__)

@inventory_bp.route('/inventory/<character_id>', methods=['GET'])
def retrieve_inventory(character_id):
    inventory = get_inventory(character_id)
    if inventory:
        return {'inventory': inventory}, 200
    else:
        return {'error': 'Inventory not found for this character'}, 404

@inventory_bp.route('/inventory/add', methods=['POST'])
def add_inventory_item():
    data = request.get_json()
    character_id = data.get('character_id')
    item = data.get('item')
    if not character_id or not item:
        return {'error': 'Character ID and item are required'}, 400
    add_item(character_id, item)
    return {'message': 'Item added to inventory'}, 200

@inventory_bp.route('/inventory/remove', methods=['POST'])
def remove_inventory_item():
    data = request.get_json()
    character_id = data.get('character_id')
    item = data.get('item')
    if not character_id or not item:
        return {'error': 'Character ID and item are required'}, 400
    remove_item(character_id, item)
    return {'message': 'Item removed from inventory'}, 200
```
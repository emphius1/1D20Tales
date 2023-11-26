```python
from flask import Blueprint, request, jsonify
from backend.database.crud_operations import get_inventory, add_item, remove_item

inventory_bp = Blueprint('inventory_bp', __name__)

@inventory_bp.route('/inventory/<character_id>', methods=['GET'])
def retrieve_inventory(character_id):
    inventory = get_inventory(character_id)
    if inventory:
        return jsonify(inventory), 200
    else:
        return jsonify({"error": "Inventory not found"}), 404

@inventory_bp.route('/inventory/add', methods=['POST'])
def add_to_inventory():
    data = request.get_json()
    character_id = data.get('character_id')
    item = data.get('item')
    result = add_item(character_id, item)
    if result:
        return jsonify({"message": "Item added successfully"}), 200
    else:
        return jsonify({"error": "Failed to add item"}), 400

@inventory_bp.route('/inventory/remove', methods=['POST'])
def remove_from_inventory():
    data = request.get_json()
    character_id = data.get('character_id')
    item = data.get('item')
    result = remove_item(character_id, item)
    if result:
        return jsonify({"message": "Item removed successfully"}), 200
    else:
        return jsonify({"error": "Failed to remove item"}), 400
```
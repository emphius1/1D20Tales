```python
from flask import Blueprint, request
from database.crud.inventory import add_item, get_item, update_item, delete_item

inventory_bp = Blueprint('inventory_bp', __name__)

@inventory_bp.route('/inventory', methods=['POST'])
def add_new_item():
    item_data = request.get_json()
    return add_item(item_data)

@inventory_bp.route('/inventory/<item_id>', methods=['GET'])
def get_single_item(item_id):
    return get_item(item_id)

@inventory_bp.route('/inventory/<item_id>', methods=['PUT'])
def update_single_item(item_id):
    item_data = request.get_json()
    return update_item(item_id, item_data)

@inventory_bp.route('/inventory/<item_id>', methods=['DELETE'])
def delete_single_item(item_id):
    return delete_item(item_id)
```
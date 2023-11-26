```python
from flask import Blueprint, request, jsonify
from backend.game_mechanics.combat import Combat

combat_blueprint = Blueprint('combat', __name__)

@combat_blueprint.route('/combat/start', methods=['POST'])
def start_combat():
    data = request.get_json()
    combat = Combat(data['character_id'], data['enemy_id'])
    combat.start()
    return jsonify({'message': 'Combat started'}), 200

@combat_blueprint.route('/combat/attack', methods=['POST'])
def attack():
    data = request.get_json()
    combat = Combat(data['character_id'], data['enemy_id'])
    result = combat.attack()
    return jsonify({'message': result}), 200

@combat_blueprint.route('/combat/defend', methods=['POST'])
def defend():
    data = request.get_json()
    combat = Combat(data['character_id'], data['enemy_id'])
    result = combat.defend()
    return jsonify({'message': result}), 200

@combat_blueprint.route('/combat/flee', methods=['POST'])
def flee():
    data = request.get_json()
    combat = Combat(data['character_id'], data['enemy_id'])
    result = combat.flee()
    return jsonify({'message': result}), 200
```
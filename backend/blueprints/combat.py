```python
from flask import Blueprint, request, jsonify
from backend.game_mechanics.combat import Combat

combat_blueprint = Blueprint('combat', __name__)

@combat_blueprint.route('/combat/start', methods=['POST'])
def start_combat():
    data = request.get_json()
    combat = Combat(data['character_id'], data['enemy_id'])
    result = combat.start()
    return jsonify(result), 200

@combat_blueprint.route('/combat/action', methods=['POST'])
def combat_action():
    data = request.get_json()
    combat = Combat(data['character_id'], data['enemy_id'])
    result = combat.action(data['action'])
    return jsonify(result), 200

@combat_blueprint.route('/combat/end', methods=['POST'])
def end_combat():
    data = request.get_json()
    combat = Combat(data['character_id'], data['enemy_id'])
    result = combat.end()
    return jsonify(result), 200
```
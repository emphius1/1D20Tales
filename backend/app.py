```python
from flask import Flask
from flask_cors import CORS
from blueprints.characters import characters_blueprint
from blueprints.inventory import inventory_blueprint
from blueprints.combat import combat_blueprint

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(characters_blueprint, url_prefix='/api/characters')
app.register_blueprint(inventory_blueprint, url_prefix='/api/inventory')
app.register_blueprint(combat_blueprint, url_prefix='/api/combat')

if __name__ == "__main__":
    app.run(debug=True)
```
```python
from flask import Flask
from flask_cors import CORS
from backend.blueprints.characters import characters_blueprint
from backend.blueprints.inventory import inventory_blueprint
from backend.blueprints.combat import combat_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(characters_blueprint, url_prefix='/api/characters')
    app.register_blueprint(inventory_blueprint, url_prefix='/api/inventory')
    app.register_blueprint(combat_blueprint, url_prefix='/api/combat')

    @app.errorhandler(404)
    def not_found(e):
        return {"message": "Not Found"}, 404

    @app.errorhandler(500)
    def server_error(e):
        return {"message": "Internal Server Error"}, 500

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
```
# SoloDungeon Project Documentation

## Backend Development

### Character Class Development

Refer to the following files for the Python classes for each D&D race, class, and background:

- `backend/character_classes/races.py`
- `backend/character_classes/classes.py`
- `backend/character_classes/backgrounds.py`

### Character Creation Logic

The system to calculate base stats based on race and class, character traits and abilities selection, and character appearance customization are implemented in the following files:

- `backend/character_creation/base_stats.py`
- `backend/character_creation/traits_abilities.py`
- `backend/character_creation/appearance.py`

### Game Mechanics Implementation

The health and mana systems, experience point calculation and leveling up algorithms, and the inventory management system are coded in:

- `backend/game_mechanics/health_mana.py`
- `backend/game_mechanics/experience_leveling.py`
- `backend/game_mechanics/inventory.py`

### Flask Application Setup

The Flask app is structured with Blueprints for different game aspects in `backend/app.py`. The blueprints are defined in:

- `backend/blueprints/characters.py`
- `backend/blueprints/inventory.py`
- `backend/blueprints/combat.py`

### API Development

API endpoints for character and inventory management, and authentication are defined and implemented in:

- `backend/api/character.py`
- `backend/api/inventory.py`
- `backend/api/authentication.py`

## Database Integration

### DynamoDB Configuration

AWS credentials setup and DynamoDB tables definition are done in `backend/database/dynamodb_config.py`.

### Database Schema Design

Detailed schemas for each table are designed in `backend/database/schemas.py`.

### CRUD Operation Implementation

Python functions for CRUD operations in DynamoDB are written in `backend/database/crud_operations.py`.

## Frontend Development

### React Project Structuring

The React project is organized into components, services, and utilities directories. Routing for different pages is set up in `frontend/src/App.js`.

### Character Customization UI

Form components for character creation, dynamic dropdowns for race and class selection, and input fields for character names, traits, and appearances are designed in:

- `frontend/src/components/CharacterCreationForm.js`
- `frontend/src/components/RaceClassDropdown.js`
- `frontend/src/components/CharacterNameTraits.js`

### Main Game UI Development

The layout for the main game interface, interactive maps, quest logs, and dialogue box components are developed in:

- `frontend/src/components/MainGameInterface.js`
- `frontend/src/components/InteractiveMap.js`
- `frontend/src/components/QuestLog.js`
- `frontend/src/components/DialogueBox.js`

### Backend Integration

Services in React for making API calls, handling API responses to update the UI, and state management for game data are implemented in:

- `frontend/src/services/api.js`
- `frontend/src/state/gameData.js`

## Enhancements and Overhauls

Enhancements to character classes, game mechanics, API functionality, and DynamoDB data layer are made in:

- `backend/enhancements/character_module.py`
- `backend/enhancements/game_mechanics.py`
- `backend/enhancements/api.py`
- `backend/enhancements/dynamodb.py`

## Testing and Debugging

Unit tests for Python modules and React components, and integration tests are written in:

- `tests/unit_tests/backend.py`
- `tests/unit_tests/frontend.js`
- `tests/integration_tests/integration.py`

## Documentation

Code documentation for the Python and React codebase is maintained in `docs/code_documentation.py`. This project documentation is regularly updated with project progress, features, and setup instructions.
```python
from backend.character_classes.races import Race
from backend.character_classes.classes import Class

class HealthManaSystem:
    def __init__(self):
        self.characters = []

    def add_character(self, character_race: Race, character_class: Class):
        character = {
            'race': character_race,
            'class': character_class,
            'health': self.calculate_health(character_race, character_class),
            'mana': self.calculate_mana(character_race, character_class)
        }
        self.characters.append(character)

    def calculate_health(self, character_race: Race, character_class: Class):
        base_health = 100
        race_health_modifier = character_race.health_modifier
        class_health_modifier = character_class.health_modifier
        return base_health + race_health_modifier + class_health_modifier

    def calculate_mana(self, character_race: Race, character_class: Class):
        base_mana = 100
        race_mana_modifier = character_race.mana_modifier
        class_mana_modifier = character_class.mana_modifier
        return base_mana + race_mana_modifier + class_mana_modifier

    def update_health(self, character_index: int, health_change: int):
        self.characters[character_index]['health'] += health_change

    def update_mana(self, character_index: int, mana_change: int):
        self.characters[character_index]['mana'] += mana_change
```
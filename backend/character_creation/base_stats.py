```python
from backend.character_classes.races import Race
from backend.character_classes.classes import Class

class BaseStats:
    def __init__(self, race: Race, class_: Class):
        self.race = race
        self.class_ = class_
        self.base_stats = self.calculate_base_stats()

    def calculate_base_stats(self):
        base_stats = {
            "strength": 10,
            "dexterity": 10,
            "constitution": 10,
            "intelligence": 10,
            "wisdom": 10,
            "charisma": 10
        }

        for stat, bonus in self.race.stat_bonuses.items():
            base_stats[stat] += bonus

        for stat, bonus in self.class_.stat_bonuses.items():
            base_stats[stat] += bonus

        return base_stats
```
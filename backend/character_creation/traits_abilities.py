```python
from backend.character_classes.races import Race
from backend.character_classes.classes import Class

class TraitsAbilities:
    def __init__(self):
        self.traits = []
        self.abilities = []

    def select_traits(self, race: Race, class_: Class):
        self.traits = race.traits + class_.traits

    def select_abilities(self, class_: Class):
        self.abilities = class_.abilities

    def get_traits(self):
        return self.traits

    def get_abilities(self):
        return self.abilities
```
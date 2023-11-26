```python
from backend.character_classes.races import Race
from backend.character_classes.classes import Class

class TraitsAbilities:
    def __init__(self):
        self.traits = []
        self.abilities = []

    def add_trait(self, trait):
        self.traits.append(trait)

    def add_ability(self, ability):
        self.abilities.append(ability)

def generate_traits_abilities(race: Race, class_: Class):
    traits_abilities = TraitsAbilities()

    for trait in race.traits:
        traits_abilities.add_trait(trait)

    for ability in class_.abilities:
        traits_abilities.add_ability(ability)

    return traits_abilities
```
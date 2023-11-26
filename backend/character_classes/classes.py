```python
class CharacterClass:
    def __init__(self, name, hit_die, primary_ability, saving_throw_proficiencies, skill_proficiencies):
        self.name = name
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.skill_proficiencies = skill_proficiencies


class Barbarian(CharacterClass):
    def __init__(self):
        super().__init__("Barbarian", 12, "Strength", ["Strength", "Constitution"], ["Athletics"])


class Bard(CharacterClass):
    def __init__(self):
        super().__init__("Bard", 8, "Charisma", ["Dexterity", "Charisma"], ["Acrobatics", "Stealth"])


class Cleric(CharacterClass):
    def __init__(self):
        super().__init__("Cleric", 8, "Wisdom", ["Wisdom", "Charisma"], ["History", "Insight"])


class Druid(CharacterClass):
    def __init__(self):
        super().__init__("Druid", 8, "Wisdom", ["Intelligence", "Wisdom"], ["Medicine", "Nature"])


class Fighter(CharacterClass):
    def __init__(self):
        super().__init__("Fighter", 10, "Strength or Dexterity", ["Strength", "Constitution"], ["Acrobatics", "Athletics"])


class Monk(CharacterClass):
    def __init__(self):
        super().__init__("Monk", 8, "Dexterity & Wisdom", ["Strength", "Dexterity"], ["Acrobatics", "Stealth"])


class Paladin(CharacterClass):
    def __init__(self):
        super().__init__("Paladin", 10, "Strength & Charisma", ["Wisdom", "Charisma"], ["Athletics", "Religion"])


class Ranger(CharacterClass):
    def __init__(self):
        super().__init__("Ranger", 10, "Dexterity & Wisdom", ["Strength", "Dexterity"], ["Nature", "Stealth"])


class Rogue(CharacterClass):
    def __init__(self):
        super().__init__("Rogue", 8, "Dexterity", ["Dexterity", "Intelligence"], ["Acrobatics", "Stealth"])


class Sorcerer(CharacterClass):
    def __init__(self):
        super().__init__("Sorcerer", 6, "Charisma", ["Constitution", "Charisma"], ["Arcana", "Deception"])


class Warlock(CharacterClass):
    def __init__(self):
        super().__init__("Warlock", 8, "Charisma", ["Wisdom", "Charisma"], ["Arcana", "Deception"])


class Wizard(CharacterClass):
    def __init__(self):
        super().__init__("Wizard", 6, "Intelligence", ["Intelligence", "Wisdom"], ["Arcana", "History"])
```
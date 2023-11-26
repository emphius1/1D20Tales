```python
class CharacterClass:
    def __init__(self, name, hit_die, primary_ability, saving_throw_proficiencies, armor_proficiencies, weapon_proficiencies, tool_proficiencies, skill_choices, skill_choices_count):
        self.name = name
        self.hit_die = hit_die
        self.primary_ability = primary_ability
        self.saving_throw_proficiencies = saving_throw_proficiencies
        self.armor_proficiencies = armor_proficiencies
        self.weapon_proficiencies = weapon_proficiencies
        self.tool_proficiencies = tool_proficiencies
        self.skill_choices = skill_choices
        self.skill_choices_count = skill_choices_count


class Barbarian(CharacterClass):
    def __init__(self):
        super().__init__("Barbarian", 12, "Strength", ["Strength", "Constitution"], ["Light armor", "Medium armor", "Shields"], ["Simple weapons", "Martial weapons"], None, ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"], 2)


class Bard(CharacterClass):
    def __init__(self):
        super().__init__("Bard", 8, "Charisma", ["Dexterity", "Charisma"], ["Light armor"], ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"], ["Three musical instruments of your choice"], ["Any"], 3)


class Cleric(CharacterClass):
    def __init__(self):
        super().__init__("Cleric", 8, "Wisdom", ["Wisdom", "Charisma"], ["Light armor", "Medium armor", "Shields"], ["Simple weapons"], None, ["History", "Insight", "Medicine", "Persuasion", "Religion"], 2)


class Druid(CharacterClass):
    def __init__(self):
        super().__init__("Druid", 8, "Wisdom", ["Intelligence", "Wisdom"], ["Light armor", "Medium armor", "Shields"], ["Clubs", "Daggers", "Darts", "Javelins", "Maces", "Quarterstaffs", "Scimitars", "Sickles", "Slings", "Spears"], ["Herbalism kit"], ["Arcana", "Animal Handling", "Insight", "Medicine", "Nature", "Perception", "Religion", "Survival"], 2)


class Fighter(CharacterClass):
    def __init__(self):
        super().__init__("Fighter", 10, "Strength or Dexterity", ["Strength", "Constitution"], ["All armor", "Shields"], ["Simple weapons", "Martial weapons"], None, ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"], 2)


class Monk(CharacterClass):
    def __init__(self):
        super().__init__("Monk", 8, "Dexterity & Wisdom", ["Strength", "Dexterity"], ["None"], ["Simple weapons", "Shortswords"], ["One type of artisan's tools or one musical instrument"], ["Acrobatics", "Athletics", "History", "Insight", "Religion", "Stealth"], 2)


class Paladin(CharacterClass):
    def __init__(self):
        super().__init__("Paladin", 10, "Strength & Charisma", ["Wisdom", "Charisma"], ["All armor", "Shields"], ["Simple weapons", "Martial weapons"], None, ["Athletics", "Insight", "Intimidation", "Medicine", "Persuasion", "Religion"], 2)


class Ranger(CharacterClass):
    def __init__(self):
        super().__init__("Ranger", 10, "Dexterity & Wisdom", ["Strength", "Dexterity"], ["Light armor", "Medium armor", "Shields"], ["Simple weapons", "Martial weapons"], None, ["Animal Handling", "Athletics", "Insight", "Investigation", "Nature", "Perception", "Stealth", "Survival"], 3)


class Rogue(CharacterClass):
    def __init__(self):
        super().__init__("Rogue", 8, "Dexterity", ["Dexterity", "Intelligence"], ["Light armor"], ["Simple weapons", "Hand crossbows", "Longswords", "Rapiers", "Shortswords"], ["Thieves' tools"], ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"], 4)


class Sorcerer(CharacterClass):
    def __init__(self):
        super().__init__("Sorcerer", 6, "Charisma", ["Constitution", "Charisma"], ["None"], ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"], None, ["Arcana", "Deception", "Insight", "Intimidation", "Persuasion", "Religion"], 2)


class Warlock(CharacterClass):
    def __init__(self):
        super().__init__("Warlock", 8, "Charisma", ["Wisdom", "Charisma"], ["Light armor"], ["Simple weapons"], None, ["Arcana", "Deception", "History", "Intimidation", "Investigation", "Nature", "Religion"], 2)


class Wizard(CharacterClass):
    def __init__(self):
        super().__init__("Wizard", 6, "Intelligence", ["Intelligence", "Wisdom"], ["None"], ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light crossbows"], None, ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"], 2)
```
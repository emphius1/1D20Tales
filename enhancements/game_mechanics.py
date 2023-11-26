```python
from backend.game_mechanics.health_mana import HealthManaSystem
from backend.game_mechanics.experience_leveling import ExperienceLevelingSystem

class EnhancedGameMechanics:
    def __init__(self):
        self.health_mana_system = HealthManaSystem()
        self.experience_leveling_system = ExperienceLevelingSystem()

    def introduce_fatigue(self, character):
        """Introduce fatigue to the character based on their actions"""
        fatigue = character.actions * 0.1
        character.stamina -= fatigue
        return character

    def manage_morale(self, character):
        """Manage the morale of the character based on their experiences"""
        morale = character.experiences * 0.05
        character.morale += morale
        return character

    def apply_environmental_effects(self, character, environment):
        """Apply environmental effects to the character"""
        if environment == 'desert':
            character.stamina -= 10
        elif environment == 'forest':
            character.stamina += 5
        return character

    def develop_skill_tree(self, character):
        """Develop a skill tree for the character"""
        skill_tree = {
            'combat': ['sword', 'archery', 'magic'],
            'crafting': ['blacksmith', 'alchemy', 'cooking'],
            'exploration': ['navigation', 'survival', 'stealth']
        }
        character.skill_tree = skill_tree
        return character

    def upgrade_ability(self, character, ability):
        """Upgrade a specific ability of the character"""
        if ability in character.abilities:
            character.abilities[ability] += 1
        return character
```
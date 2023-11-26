```python
from backend.game_mechanics.health_mana import HealthManaSystem
from backend.game_mechanics.experience_leveling import ExperienceLevelingSystem

class EnhancedHealthManaSystem(HealthManaSystem):
    def __init__(self, character_class, equipment):
        super().__init__(character_class, equipment)
        self.fatigue = 0
        self.morale = 100

    def calculate_health(self):
        super().calculate_health()
        self.health -= self.fatigue
        if self.morale < 50:
            self.health -= 10

    def calculate_mana(self):
        super().calculate_mana()
        if self.morale > 80:
            self.mana += 10

class EnhancedExperienceLevelingSystem(ExperienceLevelingSystem):
    def __init__(self, character_class, experience):
        super().__init__(character_class, experience)
        self.skill_tree = {}

    def level_up(self):
        super().level_up()
        self.skill_tree[self.level] = self.get_new_skills()

    def get_new_skills(self):
        # Logic to determine new skills based on character class and level
        pass
```
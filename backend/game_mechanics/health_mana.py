```python
class HealthManaSystem:
    def __init__(self, character_class, equipment):
        self.character_class = character_class
        self.equipment = equipment
        self.health = self.calculate_health()
        self.mana = self.calculate_mana()

    def calculate_health(self):
        base_health = self.character_class.base_health
        health_bonus = sum(item.health_bonus for item in self.equipment)
        return base_health + health_bonus

    def calculate_mana(self):
        base_mana = self.character_class.base_mana
        mana_bonus = sum(item.mana_bonus for item in self.equipment)
        return base_mana + mana_bonus

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def use_mana(self, mana_cost):
        if self.mana >= mana_cost:
            self.mana -= mana_cost
            return True
        else:
            return False

    def heal(self, healing):
        self.health += healing
        if self.health > self.calculate_health():
            self.health = self.calculate_health()

    def restore_mana(self, mana_restore):
        self.mana += mana_restore
        if self.mana > self.calculate_mana():
            self.mana = self.calculate_mana()
```
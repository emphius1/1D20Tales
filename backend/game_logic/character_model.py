```python
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other_character):
        other_character.health -= self.attack_power

    def is_alive(self):
        return self.health > 0
```
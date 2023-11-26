```python
class Race:
    def __init__(self, name, base_stats):
        self.name = name
        self.base_stats = base_stats

class Human(Race):
    def __init__(self):
        super().__init__("Human", {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 10})

class Elf(Race):
    def __init__(self):
        super().__init__("Elf", {"strength": 8, "dexterity": 12, "constitution": 10, "intelligence": 11, "wisdom": 11, "charisma": 10})

class Dwarf(Race):
    def __init__(self):
        super().__init__("Dwarf", {"strength": 12, "dexterity": 8, "constitution": 12, "intelligence": 10, "wisdom": 10, "charisma": 10})

class Halfling(Race):
    def __init__(self):
        super().__init__("Halfling", {"strength": 8, "dexterity": 12, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 12})

class Dragonborn(Race):
    def __init__(self):
        super().__init__("Dragonborn", {"strength": 12, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 8, "charisma": 12})

class Gnome(Race):
    def __init__(self):
        super().__init__("Gnome", {"strength": 8, "dexterity": 10, "constitution": 10, "intelligence": 12, "wisdom": 10, "charisma": 12})

class HalfElf(Race):
    def __init__(self):
        super().__init__("Half-Elf", {"strength": 10, "dexterity": 10, "constitution": 10, "intelligence": 10, "wisdom": 10, "charisma": 12})

class HalfOrc(Race):
    def __init__(self):
        super().__init__("Half-Orc", {"strength": 12, "dexterity": 10, "constitution": 12, "intelligence": 8, "wisdom": 10, "charisma": 10})

class Tiefling(Race):
    def __init__(self):
        super().__init__("Tiefling", {"strength": 8, "dexterity": 10, "constitution": 10, "intelligence": 12, "wisdom": 10, "charisma": 12})
```
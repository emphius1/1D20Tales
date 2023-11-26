```python
class Background:
    def __init__(self, name, skill_proficiencies, equipment, feature):
        self.name = name
        self.skill_proficiencies = skill_proficiencies
        self.equipment = equipment
        self.feature = feature


class Acolyte(Background):
    def __init__(self):
        super().__init__(
            name="Acolyte",
            skill_proficiencies=["Insight", "Religion"],
            equipment=["Holy symbol", "Prayer book", "5 sticks of incense", "Vestments", "Common clothes", "15 gp"],
            feature="Shelter of the Faithful"
        )


class Criminal(Background):
    def __init__(self):
        super().__init__(
            name="Criminal",
            skill_proficiencies=["Deception", "Stealth"],
            equipment=["Crowbar", "Dark common clothes with hood", "15 gp"],
            feature="Criminal Contact"
        )


class FolkHero(Background):
    def __init__(self):
        super().__init__(
            name="Folk Hero",
            skill_proficiencies=["Animal Handling", "Survival"],
            equipment=["Artisan's tools", "Shovel", "Iron pot", "Common clothes", "10 gp"],
            feature="Rustic Hospitality"
        )


class Noble(Background):
    def __init__(self):
        super().__init__(
            name="Noble",
            skill_proficiencies=["History", "Persuasion"],
            equipment=["Fine clothes", "Signet ring", "Scroll of pedigree", "Purse with 25 gp"],
            feature="Position of Privilege"
        )


class Sage(Background):
    def __init__(self):
        super().__init__(
            name="Sage",
            skill_proficiencies=["Arcana", "History"],
            equipment=["Bottle of black ink", "Quill", "Small knife", "Letter from a dead colleague", "Set of common clothes", "Belt pouch with 10 gp"],
            feature="Researcher"
        )


class Soldier(Background):
    def __init__(self):
        super().__init__(
            name="Soldier",
            skill_proficiencies=["Athletics", "Intimidation"],
            equipment=["Insignia of rank", "Trophy from a fallen enemy", "Set of bone dice or deck of cards", "Set of common clothes", "Belt pouch with 10 gp"],
            feature="Military Rank"
        )
```
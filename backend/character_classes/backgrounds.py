```python
class Background:
    def __init__(self, name, skill_proficiencies, languages, equipment, feature):
        self.name = name
        self.skill_proficiencies = skill_proficiencies
        self.languages = languages
        self.equipment = equipment
        self.feature = feature


class Acolyte(Background):
    def __init__(self):
        super().__init__(
            name="Acolyte",
            skill_proficiencies=["Insight", "Religion"],
            languages=2,
            equipment=["A holy symbol", "Prayer book or prayer wheel", "5 sticks of incense", "Vestments", "Common clothes", "15 gp"],
            feature="Shelter of the Faithful"
        )


class Criminal(Background):
    def __init__(self):
        super().__init__(
            name="Criminal",
            skill_proficiencies=["Deception", "Stealth"],
            languages=0,
            equipment=["A crowbar", "A set of dark common clothes including a hood", "15 gp"],
            feature="Criminal Contact"
        )


class FolkHero(Background):
    def __init__(self):
        super().__init__(
            name="Folk Hero",
            skill_proficiencies=["Animal Handling", "Survival"],
            languages=0,
            equipment=["A set of artisan's tools", "A shovel", "An iron pot", "Common clothes", "10 gp"],
            feature="Rustic Hospitality"
        )


class Noble(Background):
    def __init__(self):
        super().__init__(
            name="Noble",
            skill_proficiencies=["History", "Persuasion"],
            languages=1,
            equipment=["A set of fine clothes", "A signet ring", "A scroll of pedigree", "25 gp"],
            feature="Position of Privilege"
        )


class Sage(Background):
    def __init__(self):
        super().__init__(
            name="Sage",
            skill_proficiencies=["Arcana", "History"],
            languages=2,
            equipment=["A bottle of black ink", "A quill", "A small knife", "A letter from a dead colleague posing a question you have not yet been able to answer", "Common clothes", "10 gp"],
            feature="Researcher"
        )


class Soldier(Background):
    def __init__(self):
        super().__init__(
            name="Soldier",
            skill_proficiencies=["Athletics", "Intimidation"],
            languages=0,
            equipment=["An insignia of rank", "A trophy taken from a fallen enemy", "A set of bone dice or deck of cards", "Common clothes", "10 gp"],
            feature="Military Rank"
        )
```
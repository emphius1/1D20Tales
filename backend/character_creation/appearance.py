```python
class Appearance:
    def __init__(self, race, character_class):
        self.race = race
        self.character_class = character_class
        self.appearance_attributes = self.set_appearance_attributes()

    def set_appearance_attributes(self):
        appearance_attributes = {}

        if self.race == "Elf":
            appearance_attributes = {
                "height": "5.4",
                "weight": "130",
                "eye_color": "Green",
                "skin_color": "Light",
                "hair_color": "Blonde"
            }
        elif self.race == "Dwarf":
            appearance_attributes = {
                "height": "4.3",
                "weight": "160",
                "eye_color": "Blue",
                "skin_color": "Pale",
                "hair_color": "Brown"
            }
        elif self.race == "Human":
            appearance_attributes = {
                "height": "5.8",
                "weight": "170",
                "eye_color": "Brown",
                "skin_color": "Medium",
                "hair_color": "Black"
            }
        # Add more races as needed

        return appearance_attributes

    def customize_appearance(self, height=None, weight=None, eye_color=None, skin_color=None, hair_color=None):
        if height:
            self.appearance_attributes["height"] = height
        if weight:
            self.appearance_attributes["weight"] = weight
        if eye_color:
            self.appearance_attributes["eye_color"] = eye_color
        if skin_color:
            self.appearance_attributes["skin_color"] = skin_color
        if hair_color:
            self.appearance_attributes["hair_color"] = hair_color

    def get_appearance(self):
        return self.appearance_attributes
```
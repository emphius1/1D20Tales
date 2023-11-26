```python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

class RaceAttribute(MapAttribute):
    name = UnicodeAttribute()
    speed = NumberAttribute()
    size = UnicodeAttribute()
    languages = UnicodeAttribute()

class ClassAttribute(MapAttribute):
    name = UnicodeAttribute()
    hit_die = NumberAttribute()
    primary_ability = UnicodeAttribute()
    saving_throw_proficiencies = UnicodeAttribute()

class BackgroundAttribute(MapAttribute):
    name = UnicodeAttribute()
    skill_proficiencies = UnicodeAttribute()
    languages = UnicodeAttribute()

class CharacterModel(Model):
    class Meta:
        table_name = "characters"
        region = 'us-west-2'

    character_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    race = RaceAttribute()
    class_ = ClassAttribute()
    background = BackgroundAttribute()
    level = NumberAttribute()
    experience_points = NumberAttribute()
    hit_points = NumberAttribute()
    mana_points = NumberAttribute()
    inventory = UnicodeAttribute()
```

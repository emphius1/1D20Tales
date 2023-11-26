```python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

class CharacterModel(Model):
    class Meta:
        table_name = "characters"
        region = 'us-west-2'
    character_id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    race = UnicodeAttribute()
    class_type = UnicodeAttribute()
    background = UnicodeAttribute()
    base_stats = MapAttribute()
    traits_abilities = MapAttribute()
    appearance = MapAttribute()

class InventoryModel(Model):
    class Meta:
        table_name = "inventory"
        region = 'us-west-2'
    character_id = UnicodeAttribute(hash_key=True)
    items = MapAttribute()

class GameStateModel(Model):
    class Meta:
        table_name = "game_states"
        region = 'us-west-2'
    character_id = UnicodeAttribute(hash_key=True)
    health = NumberAttribute()
    mana = NumberAttribute()
    experience = NumberAttribute()
    level = NumberAttribute()
    location = UnicodeAttribute()
    quests = MapAttribute()
```

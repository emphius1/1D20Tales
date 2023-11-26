```python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

class GameState(Model):
    """
    This class represents the game state schema for the DynamoDB table.
    """
    class Meta:
        table_name = "game_states"
        region = 'us-west-2'  # update this to your DynamoDB region

    character_id = UnicodeAttribute(hash_key=True)
    current_level = NumberAttribute(default=1)
    current_experience = NumberAttribute(default=0)
    current_health = NumberAttribute()
    current_mana = NumberAttribute()
    current_location = MapAttribute()
    inventory = MapAttribute()
    quests = MapAttribute()
```
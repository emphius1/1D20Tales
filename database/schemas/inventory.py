```python
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute

class InventoryItem(MapAttribute):
    item_id = UnicodeAttribute()
    item_name = UnicodeAttribute()
    item_type = UnicodeAttribute()
    item_description = UnicodeAttribute()
    item_quantity = NumberAttribute()

class Inventory(Model):
    class Meta:
        table_name = 'Inventory'
        region = 'us-west-2'
    character_id = UnicodeAttribute(hash_key=True)
    items = MapAttribute(of=InventoryItem)
```
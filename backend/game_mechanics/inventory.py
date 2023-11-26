```python
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def get_items(self):
        return self.items

class Item:
    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_description(self):
        return self.description
```
```python
import openai
from game_context import GameContext
from player_actions import PlayerActions

class InventorySystem:
    def __init__(self):
        self.openai_api_key = "your-openai-api-key"
        openai.api_key = self.openai_api_key

    def generate_item_description(self, game_context: GameContext, player_actions: PlayerActions):
        prompt = f"{game_context.get_context()} {player_actions.get_actions()}"

        response = openai.Completion.create(
          engine="davinci-codex",
          prompt=prompt,
          temperature=0.5,
          max_tokens=100
        )

        return response.choices[0].text.strip()

    def add_item_to_inventory(self, item, player):
        player.inventory.append(item)
        item_description = self.generate_item_description(game_context, player_actions)
        print(f"Added {item} to inventory: {item_description}")
```

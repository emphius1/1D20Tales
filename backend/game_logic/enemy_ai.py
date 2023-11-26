```python
import openai
from game_context import GameContext
from player_actions import PlayerActions

class EnemyAISystem:
    def __init__(self):
        self.openai_api_key = "your_openai_api_key"
        openai.api_key = self.openai_api_key

    def generate_enemy_strategy(self, game_context: GameContext, player_actions: PlayerActions):
        prompt = self._create_prompt(game_context, player_actions)
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        return response.choices[0].text.strip()

    def _create_prompt(self, game_context: GameContext, player_actions: PlayerActions):
        return f"A game of D&D is in progress. The current game context is: {game_context}. The player's actions are: {player_actions}. As the enemy AI, what is your strategy?"

if __name__ == "__main__":
    enemy_ai = EnemyAISystem()
    game_context = GameContext("The player is in a dark cave with an enemy troll.")
    player_actions = PlayerActions("The player casts a fireball spell at the troll.")
    print(enemy_ai.generate_enemy_strategy(game_context, player_actions))
```
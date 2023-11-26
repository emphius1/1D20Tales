```python
import openai

class CombatSystemIntegration:
    def __init__(self, player_actions, game_context):
        self.player_actions = player_actions
        self.game_context = game_context
        self.openai_api_key = "your_openai_api_key"
        openai.api_key = self.openai_api_key

    def generate_narrative(self, character_states, combat_choices):
        prompt = self._build_prompt(character_states, combat_choices)
        response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100)
        return response.choices[0].text.strip()

    def _build_prompt(self, character_states, combat_choices):
        prompt = f"In a combat scenario, the characters are in the following states: {character_states}. "
        prompt += f"The players have chosen the following actions: {combat_choices}. "
        prompt += "As the Dungeon Master, narrate the outcomes of these actions."
        return prompt
```
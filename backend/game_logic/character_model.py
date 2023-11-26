```python
import openai
from openai.api_resources.abstract.api_resource import APIResource

class CharacterModelEnhancement(APIResource):
    def __init__(self, character_template):
        self.character_template = character_template
        self.openai = openai.OpenAI(api_key='your-api-key')

    def generate_backstory(self):
        prompt = f"Generate a unique backstory for a character with the following traits: {self.character_template}"
        response = self.openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
        return response.choices[0].text.strip()

    def generate_traits(self):
        prompt = f"Generate unique personality traits for a character with the following traits: {self.character_template}"
        response = self.openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=50)
        return response.choices[0].text.strip()
```
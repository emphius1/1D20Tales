```python
class ExperienceLeveling:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.level_up_thresholds = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]

    def gain_experience(self, amount):
        self.experience += amount
        self.check_level_up()

    def check_level_up(self):
        if self.experience >= self.level_up_thresholds[self.level]:
            self.level_up()

    def level_up(self):
        self.level += 1
        print(f"Congratulations! You've reached level {self.level}!")

    def get_current_level(self):
        return self.level

    def get_current_experience(self):
        return self.experience

    def get_experience_to_next_level(self):
        return self.level_up_thresholds[self.level] - self.experience
```
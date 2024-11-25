from utilities import generate_name, generate_skill_level, generate_random_position


class Player:
    def __init__(self, name=None, position=None, skill_level=None, total_players=0):
        # If-else structure to be able both to generate random players and to retrieve saved ones
        self.total_players = total_players
        self.name = name if name else generate_name()
        self.position = position if position else generate_random_position(total_players)
        self.skill_level = int(skill_level) if skill_level else generate_skill_level()

    def __str__(self):
        return f"{self.name} ({self.position}, Skill: {self.skill_level})"

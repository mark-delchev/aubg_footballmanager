class Team:
    def __init__(self, players, defense=0, midfield=0, attack=0):
        self.players = players  # List of Player objects
        self.defense = defense if defense else list(self.calculate_avg_skills().values())[0]
        self.midfield = midfield if midfield else list(self.calculate_avg_skills().values())[1]
        self.attack = attack if attack else list(self.calculate_avg_skills().values())[2]

    def calculate_avg_skills(self):
        # Initialize counters for each role
        defense_skills = []
        midfield_skills = []
        attack_skills = []

        for player in self.players:
            player = str(player)
            # Split the string to extract role and skill
            parts = player.split(' (')
            role = parts[1].split(',')[0]
            skill = int(parts[1].split('Skill: ')[1][:-1])  # Remove the closing parenthesis

            # Add skill to the appropriate list
            if role == 'Defender':
                defense_skills.append(skill)
            elif role == "Goalkeeper":
                defense_skills.append(skill)
            elif role == 'Midfielder':
                midfield_skills.append(skill)
            elif role == 'Attacker':
                attack_skills.append(skill)

        # Calculate averages for each role
        avg_skills = {
            'Defense': round(sum(defense_skills) / len(defense_skills)) if defense_skills else 0,
            'Midfield': round(sum(midfield_skills) / len(midfield_skills)) if midfield_skills else 0,
            'Attack': round(sum(attack_skills) / len(attack_skills)) if attack_skills else 0
        }

        return avg_skills



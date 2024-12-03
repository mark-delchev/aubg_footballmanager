import random
import unittest
from math import floor
from unittest.mock import patch, mock_open

from player import Player, Attacker, Midfielder, Defender, Goalkeeper
from team import Team
from utilities import generate_skill_level, load_names_from_csv, generate_name, add_players, generate_team_players, \
    sort_players


class TestUtil(unittest.TestCase):
    def test_load_names_from_csv(self):
        # Sample CSV data to simulate a file
        mock_csv_data = "John\nJane\nAlice\nBob\n"

        # Mock open() and simulate reading the CSV data
        with patch("builtins.open", mock_open(read_data=mock_csv_data)):
            result = load_names_from_csv("mock_file.csv")

        # Assert that the result matches the expected list
        self.assertEqual(result, ["John", "Jane", "Alice", "Bob"])

    @patch('utilities.load_names_from_csv')
    def test_generate_name(self, mock_load_names):
        # Mock the return values of load_names_from_csv
        mock_load_names.side_effect = [
            ['John', 'Jane', 'Mike'],
            ['Doe', 'Smith', 'Johnson']
        ]

        # Generate a name and assert its format
        name = generate_name()
        self.assertIsInstance(name, str)
        self.assertTrue(' ' in name)  # Ensure there's a space between first and last name

        # Test multiple generations to ensure randomness
        names = [generate_name() for _ in range(10)]
        self.assertGreater(len(set(names)), 5)  # Ensure a reasonable level of randomness

    def test_calculate_avg_skills(self):
        players = [
            Player("Player1", "Attacker", 80),
            Player("Player2", "Midfielder", 75),
        ]
        team = Team(players)
        team.calculate_avg_skills()
        self.assertEqual(team.attack, 80)
        self.assertEqual(team.midfield, 75)

    def test_generate_skill_level(self):
        # Set the seed for reproducibility
        random.seed(42)

        # Call the method under test
        result = generate_skill_level()

        # Assert that the result matches the expected value based on the seed
        expected_result = 81  # This is the expected output after running with seed=42
        self.assertEqual(result, expected_result)

    def test_add_players(self):
        players_list = []

        # Add 5 players to the list
        add_players(Attacker, 5, players_list)

        # Check the number of players
        self.assertEqual(len(players_list), 5)

        # Check the type of each player
        for player in players_list:
            self.assertIsInstance(player, Player)

        # Test with an empty initial list
        players_list = []
        add_players(Attacker, 0, players_list)
        self.assertEqual(len(players_list), 0)

    def test_player_counts(self):
        players_to_display = 22

        players = generate_team_players(players_to_display)

        # Check total player count
        self.assertEqual(len(players), players_to_display)

        # Check player type counts
        attacker_count = floor(players_to_display / 5)
        midfielder_count = floor(players_to_display / 2.5)
        defender_count = floor(players_to_display / 2.5)
        goalkeeper_count = players_to_display // 11

        attacker_count_actual = sum(1 for p in players if isinstance(p, Attacker))
        midfielder_count_actual = sum(1 for p in players if isinstance(p, Midfielder))
        defender_count_actual = sum(1 for p in players if isinstance(p, Defender))
        goalkeeper_count_actual = sum(1 for p in players if isinstance(p, Goalkeeper))

        self.assertEqual(attacker_count, attacker_count_actual)
        self.assertEqual(midfielder_count, midfielder_count_actual)
        self.assertEqual(defender_count, defender_count_actual)
        self.assertEqual(goalkeeper_count, goalkeeper_count_actual)

    def test_sort_players(self):
        players = [
            Player("Alice", "Defender"),
            Player("Bob", "Midfielder"),
            Player("Charlie", "Attacker"),
            Player("David", "Goalkeeper"),
            Player("Eve", "Defender"),
            Player("Frank", "Midfielder"),
        ]

        sorted_players = sort_players(players)

        # Check sorting order
        expected_order = ["Attacker", "Midfielder", "Defender", "Goalkeeper"]
        actual_order = [player.position for player in sorted_players]
        actual_order_no_duplicates = []

        for player_position in actual_order:
            if player_position not in actual_order_no_duplicates:
                actual_order_no_duplicates.append(player_position)
        self.assertEqual(expected_order, actual_order_no_duplicates)

        # Check alphabetical sorting within positions
        midfielders = [player for player in sorted_players if player.position == "Midfielder"]
        self.assertEqual(["Bob", "Frank"], [player.name for player in midfielders])

        # Check original list is not modified
        self.assertEqual(players[0].position, "Defender")


if __name__ == "__main__":
    unittest.main()

import unittest
from collections import Counter
from random import seed
from utilities import generate_random_position


class TestGenerateRandomPosition(unittest.TestCase):

    def test_goalkeeper_presence(self):
        seed(0)  # Ensures consistent randomness for the test
        total_players = 22
        iterations = 2
        """
        for _ in range(iterations):
            # Generate a list of positions for each iteration
            positions = [generate_random_position(total_players) for _ in range(total_players)]

            # Check that "Goalkeeper" is in the list for each team
            self.assertIn("Goalkeeper", positions,
                          f"Generated list of positions does not include a 'Goalkeeper' for total_players = {total_players}")
        """



if __name__ == "__main__":
    unittest.main()

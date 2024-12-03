import csv
import player

from math import floor, ceil
from random import randint, choices, choice


# File with helper functions

# Player Name generator


def load_names_from_csv(file_path):
    first_names = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            first_names.append(row[0])  # Assuming the first name is in the first column
    return first_names


# Load the names from CSV file
first_names_list = load_names_from_csv('first_names.csv')
last_names_list = load_names_from_csv('last_names.csv')


def generate_name():
    player_name = choice(first_names_list) + " " + choice(last_names_list)
    return player_name


def generate_skill_level():
    return randint(0, 100)


def add_players(player_class, count, players_list):
    for _ in range(count):
        players_list.append(player_class())


def generate_random_position(total_players):
    # Absolute counts for each position
    remaining_slots = {
        "Goalkeeper": floor(total_players / 10),
        "Defender": ceil(total_players / 3),
        "Midfielder": ceil(total_players / 3),
        "Attacker": floor(total_players / 4),
    }

    # Flatten the list of positions based on absolute counts
    available_positions = (
            ["Goalkeeper"] * remaining_slots["Goalkeeper"] +
            ["Defender"] * remaining_slots["Defender"] +
            ["Midfielder"] * remaining_slots["Midfielder"] +
            ["Attacker"] * remaining_slots["Attacker"]
    )

    # Randomly select one position
    return choices(available_positions, k=1)[0]


# Function that generates a determined proportion of players to be displayed in select_players method
def generate_team_players(players_to_display):
    players = []
    add_players(player.Attacker, (players_to_display // 5), players)
    add_players(player.Midfielder, floor(players_to_display / 2.5), players)
    add_players(player.Defender, floor(players_to_display / 2.5), players)
    add_players(player.Goalkeeper, players_to_display // 11, players)
    return players


# Sort players top to bottom from Attacker to Goalkeeper
def sort_players(player_lst):
    position_order = {"Attacker": 0, "Midfielder": 1, "Defender": 2, "Goalkeeper": 3}
    sorted_players = sorted(player_lst, key=lambda p: position_order[p.position])
    return sorted_players

import csv
import random

from math import floor, ceil
import tkinter as tk
from faker import Faker
from transliterate import translit
from random import randint, choices


# File with helper functions

fake = Faker("bg_BG")

# Player Name generator
# NOTE: the library used (faker) produces strange names on purpose


def load_first_names_from_csv(file_path):
    first_names = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            first_names.append(row[0])  # Assuming the first name is in the first column
    return first_names


# Load the first names from your CSV file (e.g., 'names.csv')
first_names_list = load_first_names_from_csv('first_names.csv')


def generate_name():
    player_name = random.choice(first_names_list) + " " + fake.last_name_male()
    player_name = translit(player_name, 'bg', reversed=True)
    # print(player_name)
    return player_name


def generate_skill_level():
    return randint(0, 100)


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




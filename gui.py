import csv
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import team
from player import Player
from team import Team

class FootballManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Football Manager")
        self.player_check_states = {}
        # Example navigation: Main menu
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        frame = tk.Frame(self.root)
        frame.pack(pady=20, padx=20)

        # Button to select players
        btn_view_teams = ttk.Button(frame, text="Select Players", command=self.select_players)
        btn_view_teams.pack(pady=5)

        # Button to load selected players from csv file
        btn_view_matches = ttk.Button(frame, text="Load Players", command=self.view_matches)
        btn_view_matches.pack(pady=5)

        # Button to quit
        btn_quit = ttk.Button(frame, text="Quit", command=self.root.quit)
        btn_quit.pack(pady=5)

    def select_players(self):
        # Clear the current window
        self.clear_window()
        label = tk.Label(self.root, text="Select 11 players (1 of them a goalkeeper)", font=("Arial", 16))
        label.pack(pady=20)
        players_to_display = 22
        players = [Player(total_players=players_to_display) for _ in range(players_to_display)]
        position_order = {"Attacker": 0, "Midfielder": 1, "Defender": 2, "Goalkeeper": 3}
        sorted_players = sorted(players, key=lambda p: position_order[p.position])
        # Create a frame for the grid
        grid_frame = tk.Frame(self.root)
        grid_frame.pack(pady=10, padx=10)

        # Define the number of columns
        num_columns = 2
        for index, player in enumerate(sorted_players):
            checkbox = tk.BooleanVar()  # Track the state of the checkbox
            self.player_check_states[player] = checkbox

            # Calculate row and column
            row = index // num_columns
            col = index % num_columns

            # Add a Checkbutton to the grid
            chk = tk.Checkbutton(grid_frame, text=str(player), variable=checkbox, font=("Arial", 11))
            chk.grid(row=row, column=col, pady=2, sticky="w")

        btn_save = ttk.Button(self.root, text="Save Selected Players", command=self.save_selected_players)
        btn_save.pack(pady=10)

        # Back button to return to the main menu
        btn_back = ttk.Button(self.root, text="Back to Main Menu", command=self.create_main_menu)
        btn_back.pack(pady=10)

    def view_matches(self):
        """
        Placeholder function for viewing matches.
        """
        # Clear the current window
        self.clear_window()

        label = tk.Label(self.root, text="Match details will be displayed here.", font=("Arial", 16))
        label.pack(pady=20)

        with open("selected_players.csv", 'r') as file:
            reader = csv.DictReader(file)
            # Read all rows from CSV, create Player objects, and get the first 11 players
            players = [Player(row['Name'], row['Position'], row['Skill']) for row in reader]

        strings = players
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10)
        # Row 1 - 2 strings
        row1 = tk.Frame(frame)
        row1.pack(pady=5)
        for string in strings[:2]:
            label = tk.Label(row1, text=string)
            label.pack(side=tk.LEFT, padx=5)

        # Row 2 - 4 strings
        row2 = tk.Frame(frame)
        row2.pack(pady=5)
        for string in strings[2:6]:
            label = tk.Label(row2, text=string)
            label.pack(side=tk.LEFT, padx=5)

        # Row 3 - 4 strings
        row3 = tk.Frame(frame)
        row3.pack(pady=5)
        for string in strings[6:10]:
            label = tk.Label(row3, text=string)
            label.pack(side=tk.LEFT, padx=5)

        # Row 4 - 1 string
        row4 = tk.Frame(frame)
        row4.pack(pady=5)
        label = tk.Label(row4, text=strings[10])
        label.pack()

        team = Team(players=players)
        team.calculate_avg_skills()

        label = tk.Label(self.root, text=f"Attack: {team.attack}", font=("Arial", 11))
        label.pack(pady=5)
        label = tk.Label(self.root, text=f"Midfield: {team.midfield}", font=("Arial", 11))
        label.pack(pady=5)
        label = tk.Label(self.root, text=f"Defense: {team.defense}", font=("Arial", 11))
        label.pack(pady=5)



    def clear_window(self):
        """
        Clears all widgets in the current window.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def save_selected_players(self):
        """
        Save the marked players to a CSV file.
        """
        selected_players = [player for player, var in self.player_check_states.items() if var.get()]
        goalkeepers = [player for player in selected_players if player.position == "Goalkeeper"]
        selection_error = False

        if len(selected_players) != 11:
            # Show a warning if the number of players is not 11
            selection_error = True
            messagebox.showwarning("Invalid Selection", f"Exactly 11 players must be selected. \
You selected {len(selected_players)}.")
        if len(goalkeepers) != 1:
            selection_error = True
            messagebox.showwarning("Save failed", f"Exactly 1 goalkeeper must be selected. \
You selected {len(goalkeepers)}.")
        if not selection_error:
            with open("selected_players.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "Position", "Skill"])  # Replace with actual attributes
                for player in selected_players:
                    writer.writerow([player.name, player.position, player.skill_level])

            messagebox.showinfo("Save successful", f"Saved 11 players (including 1 goalkeeper) \
to 'selected_players.csv'.")
            messagebox.showinfo("Continue", "After this click on back to menu and load \
your save file")


def main(window_size):
    root = tk.Tk()
    root.geometry(window_size)
    FootballManagerApp(root)
    root.mainloop()

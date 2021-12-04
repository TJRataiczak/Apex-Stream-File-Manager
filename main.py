import tkinter as tk
import json
import os

class Application:

    def __init__(self, root):
        root.title("Apex Stream Manager")
        # photo = tk.PhotoImage(file="apex_photo.png")
        # root.iconphoto(False, photo)
        mainframe = tk.Frame(root)
        mainframe.grid(column=0, row=0)

        # Setting up first player
        self.seat_a_player_a_title_label = tk.Label(mainframe, text="Seat A Player A").grid(column=0, row=0, padx=50)
        self.seat_a_player_a_current_name = tk.StringVar()
        self.seat_a_player_a_name_label = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_name).grid(column=0, row=1, padx=50)
        self.seat_a_player_a_current_deck = tk.StringVar()
        self.seat_a_player_a_deck_label = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_deck).grid(column=0, row=2, padx=50)
        #Setting up second player
        self.seat_a_player_b_title_label = tk.Label(mainframe, text="Seat A Player B").grid(column=0, row=3, padx=50)
        self.seat_a_player_b_current_name = tk.StringVar()
        self.seat_a_player_b_name_label = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_name).grid(column=0, row=4, padx=50)
        self.seat_a_player_b_current_deck = tk.StringVar()
        self.seat_a_player_b_deck_label = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_deck).grid(column=0, row=5, padx=50)

        # Setting up third player
        self.seat_b_player_a_title_label = tk.Label(mainframe, text="Seat B Player A").grid(column=1, row=0)
        self.seat_b_player_a_current_name = tk.StringVar()
        self.seat_b_player_a_name_label = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_name).grid(column=1, row=1, padx=50)
        self.seat_b_player_a_current_deck = tk.StringVar()
        self.seat_b_player_a_deck_label = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_deck).grid(column=1, row=2, padx=50)
        #Setting up fourth player
        self.seat_b_player_b_title_label = tk.Label(mainframe, text="Seat B Player B").grid(column=1, row=3, padx=50)
        self.seat_b_player_b_current_name = tk.StringVar()
        self.seat_b_player_b_name_label = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_name).grid(column=1, row=4, padx=50)
        self.seat_b_player_b_current_deck = tk.StringVar()
        self.seat_b_player_b_deck_label = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_deck).grid(column=1, row=5, padx=50)

        # Setting up fifth player
        self.seat_c_player_a_title_label = tk.Label(mainframe, text="Seat C Player A").grid(column=2, row=0)
        self.seat_c_player_a_current_name = tk.StringVar()
        self.seat_c_player_a_name_label = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_name).grid(column=2, row=1, padx=50)
        self.seat_c_player_a_current_deck = tk.StringVar()
        self.seat_c_player_a_deck_label = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_deck).grid(column=2, row=2, padx=50)
        #Setting up sixth player
        self.seat_c_player_b_title_label = tk.Label(mainframe, text="Seat C Player B").grid(column=2, row=3, padx=50)
        self.seat_c_player_b_current_name = tk.StringVar()
        self.seat_c_player_b_name_label = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_name).grid(column=2, row=4, padx=50)
        self.seat_c_player_b_current_deck = tk.StringVar()
        self.seat_c_player_b_deck_label = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_deck).grid(column=2, row=5, padx=50)

        #Setting up lifetotals left side
        self.lifetotal_left_current = tk.StringVar()
        self.lifetotal_left_current.set("Lifetotal: 20")
        self.lifetotal_left_label = tk.Label(mainframe, textvariable=self.lifetotal_left_current).grid(column=0, row=6, pady=10)

        #Setting up lifetotals right side
        self.lifetotal_right_current = tk.StringVar()
        self.lifetotal_right_current.set("Lifetotal: 20")
        self.lifetotal_right_label = tk.Label(mainframe, textvariable=self.lifetotal_left_current).grid(column=2, row=6, pady=10)

        self.load_settings()

    #Loads from settings.json and gets the text files they are using
    def load_settings(self):
        with open("settings.json") as f:
            settings = json.load(f)
            self.seat_a_player_a_name_file = settings["seatAPlayerAName"]
            self.seat_a_player_a_deck_file = settings["seatAPlayerADeck"]
            self.seat_a_player_a_name_file = settings["seatAPlayerBName"]
            self.seat_a_player_a_deck_file = settings["seatAPlayerBDeck"]
            self.seat_a_player_a_name_file = settings["seatBPlayerAName"]
            self.seat_a_player_a_deck_file = settings["seatBPlayerADeck"]
            self.seat_a_player_a_name_file = settings["seatBPlayerBName"]
            self.seat_a_player_a_deck_file = settings["seatBPlayerBDeck"]
            self.seat_a_player_a_name_file = settings["seatCPlayerAName"]
            self.seat_a_player_a_deck_file = settings["seatCPlayerADeck"]
            self.seat_a_player_a_name_file = settings["seatCPlayerBName"]
            self.seat_a_player_a_deck_file = settings["seatCPlayerBDeck"]

root = tk.Tk()
Application(root)
root.mainloop()
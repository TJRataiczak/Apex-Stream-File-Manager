import tkinter as tk
import json

class Application:

    DIRECTORY = "Stream Files/"

    def __init__(self, root):
        
        self.load_settings()
        
        root.title("Apex Stream Manager")
        # photo = tk.PhotoImage(file="apex_photo.png")
        # root.iconphoto(False, photo)
        mainframe = tk.Frame(root)
        mainframe.grid(column=0, row=0)

        # Setting up first player
        self.seat_a_player_a_title_label = tk.Label(mainframe, text="Seat A Player A").grid(column=0, row=0, padx=50)
        self.seat_a_player_a_current_name = tk.StringVar()
        self.seat_a_player_a_name_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_name).grid(column=0, row=1, padx=50)
        self.seat_a_player_a_current_deck = tk.StringVar()
        self.seat_a_player_a_deck_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_deck).grid(column=0, row=2, padx=50)
        
        #Setting up second player
        self.seat_a_player_b_title_label = tk.Label(mainframe, text="Seat A Player B").grid(column=0, row=3, padx=50)
        self.seat_a_player_b_current_name = tk.StringVar()
        self.seat_a_player_b_name_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_name).grid(column=0, row=4, padx=50)
        self.seat_a_player_b_current_deck = tk.StringVar()
        self.seat_a_player_b_deck_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_deck).grid(column=0, row=5, padx=50)

        # Setting up third player
        self.seat_b_player_a_title_label = tk.Label(mainframe, text="Seat B Player A").grid(column=1, row=0)
        self.seat_b_player_a_current_name = tk.StringVar()
        self.seat_b_player_a_name_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_name).grid(column=1, row=1, padx=50)
        self.seat_b_player_a_current_deck = tk.StringVar()
        self.seat_b_player_a_deck_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_deck).grid(column=1, row=2, padx=50)
        #Setting up fourth player
        self.seat_b_player_b_title_label = tk.Label(mainframe, text="Seat B Player B").grid(column=1, row=3, padx=50)
        self.seat_b_player_b_current_name = tk.StringVar()
        self.seat_b_player_b_name_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_name).grid(column=1, row=4, padx=50)
        self.seat_b_player_b_current_deck = tk.StringVar()
        self.seat_b_player_b_deck_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_deck).grid(column=1, row=5, padx=50)

        # Setting up fifth player
        self.seat_c_player_a_title_label = tk.Label(mainframe, text="Seat C Player A").grid(column=2, row=0)
        self.seat_c_player_a_current_name = tk.StringVar()
        self.seat_c_player_a_name_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_name).grid(column=2, row=1, padx=50)
        self.seat_c_player_a_current_deck = tk.StringVar()
        self.seat_c_player_a_deck_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_deck).grid(column=2, row=2, padx=50)
        #Setting up sixth player
        self.seat_c_player_b_title_label = tk.Label(mainframe, text="Seat C Player B").grid(column=2, row=3, padx=50)
        self.seat_c_player_b_current_name = tk.StringVar()
        self.seat_c_player_b_name_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_name).grid(column=2, row=4, padx=50)
        self.seat_c_player_b_current_deck = tk.StringVar()
        self.seat_c_player_b_deck_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_deck).grid(column=2, row=5, padx=50)

        #Setting up lifetotals left side
        self.lifetotal_left_current = tk.StringVar()
        self.lifetotal_left_label = tk.Label(mainframe, textvariable=self.lifetotal_left_current).grid(column=0, row=6, pady=10)
        self.lifetotal_left_reset = tk.Button(mainframe, text= "20", command=lambda:self.update_life_total(self.left_lifetotal_file, 20, "left"), width=15).grid(column=0, row=7)
        self.lifetotal_left_add_three = tk.Button(mainframe, text= "3", command=lambda:self.update_life_total(self.left_lifetotal_file, 3, "left"), width=15).grid(column=0, row=8)
        self.lifetotal_left_add_one = tk.Button(mainframe, text= "1", command=lambda:self.update_life_total(self.left_lifetotal_file, 1, "left"), width=15).grid(column=0, row=9)
        self.lifetotal_left_minus_one = tk.Button(mainframe, text= "-1", command=lambda:self.update_life_total(self.left_lifetotal_file, -1, "left"), width=15).grid(column=0, row=10)
        self.lifetotal_left_minus_three = tk.Button(mainframe, text= "-3", command=lambda:self.update_life_total(self.left_lifetotal_file, -3, "left"), width=15).grid(column=0, row=11)

        #Setting up lifetotals right side
        self.lifetotal_right_current = tk.StringVar()
        self.lifetotal_right_label = tk.Label(mainframe, textvariable=self.lifetotal_right_current).grid(column=2, row=6, pady=10)
        self.lifetotal_right_reset = tk.Button(mainframe, text= "20", command=lambda:self.update_life_total(self.right_lifetotal_file, 20, "right"), width=15).grid(column=2, row=7)
        self.lifetotal_right_add_three = tk.Button(mainframe, text= "3", command=lambda:self.update_life_total(self.right_lifetotal_file, 3, "right"), width=15).grid(column=2, row=8)
        self.lifetotal_right_add_one = tk.Button(mainframe, text= "1", command=lambda:self.update_life_total(self.right_lifetotal_file, 1, "right"), width=15).grid(column=2, row=9)
        self.lifetotal_right_minus_one = tk.Button(mainframe, text= "-1", command=lambda:self.update_life_total(self.right_lifetotal_file, -1, "right"), width=15).grid(column=2, row=10)
        self.lifetotal_right_minus_three = tk.Button(mainframe, text= "-3", command=lambda:self.update_life_total(self.right_lifetotal_file, -3, "right"), width=15).grid(column=2, row=11)

        #Setting up records, commentators and update
        self.left_record_label = tk.Label(mainframe, text="Left Record").grid(column=1, row=6)
        self.left_record_current = tk.StringVar()
        self.left_record_entry = tk.Entry(mainframe, textvariable=self.left_record_current).grid(column=1, row=7)
        self.right_record_label = tk.Label(mainframe, text="Right Record").grid(column=1, row=8)
        self.right_record_current = tk.StringVar()
        self.right_record_entry = tk.Entry(mainframe, textvariable=self.right_record_current).grid(column=1, row=9)
        self.commentator_label = tk.Label(mainframe, text="Commentator(s)").grid(column=1, row=10)
        self.commentator_current = tk.StringVar()
        self.commentator_entry = tk.Entry(mainframe, textvariable=self.commentator_current).grid(column=1, row=11)
        self.update_button = tk.Button(mainframe, text="Update", command=self.update_player_data, width=15).grid(column=1, row=12, pady=15)

    #Loads from settings.json and gets the text files they are using
    def load_settings(self):
        with open(f"{self.DIRECTORY}settings.json") as f:
            settings = json.load(f)
            self.seat_a_player_a_name_file = settings["seatAPlayerAName"]
            self.seat_a_player_a_deck_file = settings["seatAPlayerADeck"]
            self.seat_a_player_b_name_file = settings["seatAPlayerBName"]
            self.seat_a_player_b_deck_file = settings["seatAPlayerBDeck"]
            self.seat_b_player_a_name_file = settings["seatBPlayerAName"]
            self.seat_b_player_a_deck_file = settings["seatBPlayerADeck"]
            self.seat_b_player_b_name_file = settings["seatBPlayerBName"]
            self.seat_b_player_b_deck_file = settings["seatBPlayerBDeck"]
            self.seat_c_player_a_name_file = settings["seatCPlayerAName"]
            self.seat_c_player_a_deck_file = settings["seatCPlayerADeck"]
            self.seat_c_player_b_name_file = settings["seatCPlayerBName"]
            self.seat_c_player_b_deck_file = settings["seatCPlayerBDeck"]
            self.left_lifetotal_file = settings["leftLifeTotal"]
            self.right_lifetotal_file = settings["rightLifeTotal"]
            self.left_record_file = settings["leftRecord"]
            self.right_record_file = settings["rightRecord"]
            self.commentator_file = settings["commentator"]
    
    def update_player_data(self):
        if self.seat_a_player_a_current_name.get() != "":
            self.write_data_to_file(self.seat_a_player_a_name_file, self.seat_a_player_a_current_name.get())
            self.seat_a_player_a_current_name.set("")
        
        if self.seat_a_player_a_current_deck.get() != "":
            self.write_data_to_file(self.seat_a_player_a_deck_file, self.seat_a_player_a_current_deck.get())
            self.seat_a_player_a_current_deck.set("")
        
        if self.seat_a_player_b_current_name.get() != "":
            self.write_data_to_file(self.seat_a_player_b_name_file, self.seat_a_player_b_current_name.get())
            self.seat_a_player_b_current_name.set("")
        
        if self.seat_a_player_b_current_deck.get() != "":
            self.write_data_to_file(self.seat_a_player_b_deck_file, self.seat_a_player_b_current_deck.get())
            self.seat_a_player_b_current_deck.set("")
        
        if self.seat_b_player_a_current_name.get() != "":
            self.write_data_to_file(self.seat_b_player_a_name_file, self.seat_b_player_a_current_name.get())
            self.seat_b_player_a_current_name.set("")
        
        if self.seat_b_player_a_current_deck.get() != "":
            self.write_data_to_file(self.seat_b_player_a_deck_file, self.seat_b_player_a_current_deck.get())
            self.seat_b_player_a_current_deck.set("")
        
        if self.seat_b_player_b_current_name.get() != "":
            self.write_data_to_file(self.seat_b_player_b_name_file, self.seat_b_player_b_current_name.get())
            self.seat_b_player_b_current_name.set("")
        
        if self.seat_b_player_b_current_deck.get() != "":
            self.write_data_to_file(self.seat_b_player_b_deck_file, self.seat_b_player_b_current_deck.get())
            self.seat_b_player_b_current_deck.set("")
        
        if self.seat_c_player_a_current_name.get() != "":
            self.write_data_to_file(self.seat_c_player_a_name_file, self.seat_c_player_a_current_name.get())
            self.seat_c_player_a_current_name.set("")
        
        if self.seat_c_player_a_current_deck.get() != "":
            self.write_data_to_file(self.seat_c_player_a_deck_file, self.seat_c_player_a_current_deck.get())
            self.seat_c_player_a_current_deck.set("")
        
        if self.seat_c_player_b_current_name.get() != "":
            self.write_data_to_file(self.seat_c_player_b_name_file, self.seat_c_player_b_current_name.get())
            self.seat_c_player_b_current_name.set("")
        
        if self.seat_c_player_b_current_deck.get() != "":
            self.write_data_to_file(self.seat_c_player_b_deck_file, self.seat_c_player_b_current_deck.get())
            self.seat_c_player_b_current_deck.set("")
        
        if self.left_record_current.get() != "":
            self.write_data_to_file(self.left_record_file, self.left_record_current.get())
            self.left_record_current.set("")
        
        if self.right_record_current.get() != "":
            self.write_data_to_file(self.right_record_file, self.right_record_current.get())
            self.right_record_current.set("")

        if self.commentator_current.get() != "":
            self.write_data_to_file(self.commentator_file, self.commentator_current.get())
            self.commentator_current.set("")
        
    
    def write_data_to_file(self, filename, new_value):
        with open(f"{self.DIRECTORY}{filename}", "w") as f:
            f.write(new_value)
    
    def update_life_total(self, filename, amount, side):
        with open(f"{self.DIRECTORY}{filename}", "r") as f:
            life_total_value = int(f.read())
        
        with open(f"{self.DIRECTORY}{filename}", "w") as f:
            if amount == 20:
                f.write("20")
            else:
                amount = str(life_total_value + amount)
                f.write(amount)

        if side == "left":
            self.lifetotal_left_current.set(f"Lifetotal: {amount}")
        elif side == "right":
            self.lifetotal_right_current.set(f"Lifetotal: {amount}")

root = tk.Tk()
Application(root)
root.mainloop()
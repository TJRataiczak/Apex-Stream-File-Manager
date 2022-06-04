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

        #Labeling columns
        self.top_player_label = tk.Label(mainframe, text="Name").grid(column=0, row=1, padx=50)
        self.top_deck_label = tk.Label(mainframe, text="Deck").grid(column=0, row=2, padx=50)
        self.top_record_label = tk.Label(mainframe, text="Record").grid(column=0, row=3, padx=50)
        self.top_lifetotal_label = tk.Label(mainframe, text="Lifetotal").grid(column=0, row=4, padx=50)
        self.bottom_player_label = tk.Label(mainframe, text="Name").grid(column=0, row=6, padx=50)
        self.bottom_deck_label = tk.Label(mainframe, text="Deck").grid(column=0, row=7, padx=50)
        self.bottom_record_label = tk.Label(mainframe, text="Record").grid(column=0, row=8, padx=50)
        self.bottom_lifetotal_label = tk.Label(mainframe, text="Lifetotal").grid(column=0, row=9, padx=50)

        # Setting up first player
        self.seat_a_player_a_title_label = tk.Label(mainframe, text="Seat A Player A").grid(column=1, row=0, padx=(0, 50))
        self.seat_a_player_a_current_name = tk.StringVar()
        self.seat_a_player_a_name_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_name).grid(column=1, row=1, padx=(0, 50))
        self.seat_a_player_a_current_deck = tk.StringVar()
        self.seat_a_player_a_deck_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_deck).grid(column=1, row=2, padx=(0, 50))
        self.seat_a_player_a_current_record = tk.StringVar()
        self.seat_a_player_a_record_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_record).grid(column=1, row=3, padx=(0, 50))
        self.seat_a_player_a_current_lifetotal = tk.StringVar()
        self.seat_a_player_a_lifetotal_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_a_current_lifetotal).grid(column=1, row=4, padx=(0, 50))
        
        #Setting up second player
        self.seat_a_player_b_title_label = tk.Label(mainframe, text="Seat A Player B").grid(column=1, row=5, padx=(0, 50))
        self.seat_a_player_b_current_name = tk.StringVar()
        self.seat_a_player_b_name_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_name).grid(column=1, row=6, padx=(0, 50))
        self.seat_a_player_b_current_deck = tk.StringVar()
        self.seat_a_player_b_deck_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_deck).grid(column=1, row=7, padx=(0, 50))
        self.seat_a_player_b_current_record = tk.StringVar()
        self.seat_a_player_b_record_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_record).grid(column=1, row=8, padx=(0, 50))
        self.seat_a_player_b_current_lifetotal = tk.StringVar()
        self.seat_a_player_b_lifetotal_entry = tk.Entry(mainframe, textvariable = self.seat_a_player_b_current_lifetotal).grid(column=1, row=9, padx=(0, 50))

        # Setting up third player
        self.seat_b_player_a_title_label = tk.Label(mainframe, text="Seat B Player A").grid(column=2, row=0, padx=50)
        self.seat_b_player_a_current_name = tk.StringVar()
        self.seat_b_player_a_name_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_name).grid(column=2, row=1, padx=50)
        self.seat_b_player_a_current_deck = tk.StringVar()
        self.seat_b_player_a_deck_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_deck).grid(column=2, row=2, padx=50)
        self.seat_b_player_a_current_record = tk.StringVar()
        self.seat_b_player_a_record_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_record).grid(column=2, row=3, padx=50)
        self.seat_b_player_a_current_lifetotal = tk.StringVar()
        self.seat_b_player_a_lifetotal_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_a_current_lifetotal).grid(column=2, row=4, padx=50)
        
        #Setting up fourth player
        self.seat_b_player_b_title_label = tk.Label(mainframe, text="Seat B Player B").grid(column=2, row=5, padx=50)
        self.seat_b_player_b_current_name = tk.StringVar()
        self.seat_b_player_b_name_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_name).grid(column=2, row=6, padx=50)
        self.seat_b_player_b_current_deck = tk.StringVar()
        self.seat_b_player_b_deck_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_deck).grid(column=2, row=7, padx=50)
        self.seat_b_player_b_current_record = tk.StringVar()
        self.seat_b_player_b_record_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_record).grid(column=2, row=8, padx=50)
        self.seat_b_player_b_current_lifetotal = tk.StringVar()
        self.seat_b_player_b_lifetotal_entry = tk.Entry(mainframe, textvariable = self.seat_b_player_b_current_lifetotal).grid(column=2, row=9, padx=50)

        # Setting up fifth player
        self.seat_c_player_a_title_label = tk.Label(mainframe, text="Seat C Player A").grid(column=3, row=0, padx=50)
        self.seat_c_player_a_current_name = tk.StringVar()
        self.seat_c_player_a_name_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_name).grid(column=3, row=1, padx=50)
        self.seat_c_player_a_current_deck = tk.StringVar()
        self.seat_c_player_a_deck_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_deck).grid(column=3, row=2, padx=50)
        self.seat_c_player_a_current_record = tk.StringVar()
        self.seat_c_player_a_record_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_record).grid(column=3, row=3, padx=50)
        self.seat_c_player_a_current_lifetotal = tk.StringVar()
        self.seat_c_player_a_lifetotal_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_a_current_lifetotal).grid(column=3, row=4, padx=50)
        
        #Setting up sixth player
        self.seat_c_player_b_title_label = tk.Label(mainframe, text="Seat C Player B").grid(column=3, row=5, padx=50)
        self.seat_c_player_b_current_name = tk.StringVar()
        self.seat_c_player_b_name_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_name).grid(column=3, row=6, padx=50)
        self.seat_c_player_b_current_deck = tk.StringVar()
        self.seat_c_player_b_deck_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_deck).grid(column=3, row=7, padx=50)
        self.seat_c_player_b_current_record = tk.StringVar()
        self.seat_c_player_b_record_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_record).grid(column=3, row=8, padx=50)
        self.seat_c_player_b_current_lifetotal = tk.StringVar()
        self.seat_c_player_b_lifetotal_entry = tk.Entry(mainframe, textvariable = self.seat_c_player_b_current_lifetotal).grid(column=3, row=9, padx=50)

        #Setting up left lifetotal
        self.left_lifetotal_reset = tk.Button(mainframe, text="20", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_left, 20), width=15).grid(column=1, row=10, pady=(40, 0), padx=(0, 50))
        self.left_lifetotal_add_two = tk.Button(mainframe, text="2", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_left, 2), width=15).grid(column=1, row=11, padx=(0, 50))
        self.left_lifetotal_add_one = tk.Button(mainframe, text="1", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_left, 1), width=15).grid(column=1, row=12, padx=(0, 50))
        self.left_lifetotal_subtract_one = tk.Button(mainframe, text="-1", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_left, -1), width=15).grid(column=1, row=13, padx=(0, 50))
        self.left_lifetotal_subtract_two = tk.Button(mainframe, text="-2", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_left, -2), width=15).grid(column=1, row=14, pady=(0, 20), padx=(0, 50))

        #Setting up right lifetotal
        self.right_lifetotal_reset = tk.Button(mainframe, text="20", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_right, 20), width=15).grid(column=3, row=10, pady=(40, 0))
        self.right_lifetotal_add_two = tk.Button(mainframe, text="2", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_right, 2), width=15).grid(column=3, row=11)
        self.right_lifetotal_add_one = tk.Button(mainframe, text="1", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_right, 1), width=15).grid(column=3, row=12)
        self.right_lifetotal_subtract_one = tk.Button(mainframe, text="-1", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_right, -1), width=15).grid(column=3, row=13)
        self.right_lifetotal_subtract_two = tk.Button(mainframe, text="-2", command=lambda:self.change_current_lifetotal(self.adjustable_lifetotal_right, -2), width=15).grid(column=3, row=14, pady=(0, 20))

        #Update and lifetotal change buttons
        self.current_lifetotal_text = tk.StringVar()
        self.current_lifetotal_text.set("Match A")
        self.current_lifetotal_label = tk.Label(mainframe, textvariable=self.current_lifetotal_text).grid(column=2, row=10, pady=(40, 0))
        self.lifetotal_match_a = tk.Button(mainframe, text="Match A Lifetotal", command=lambda:self.change_current_lifetotal_file("a"), width=15).grid(column=2, row=11)
        self.lifetotal_match_b = tk.Button(mainframe, text="Match B Lifetotal", command=lambda:self.change_current_lifetotal_file("b"), width=15).grid(column=2, row=12)
        self.lifetotal_match_c = tk.Button(mainframe, text="Match C Lifetotal", command=lambda:self.change_current_lifetotal_file("c"), width=15).grid(column=2, row=13)
        self.update_button = (tk.Button(mainframe, text="Update", command=lambda:self.update_player_data(), width=15).grid(column=2, row=14, pady=(0, 20)))

    #Loads from settings.json and gets the text files they are using
    def load_settings(self):
        with open(f"{self.DIRECTORY}settings.json") as f:
            settings = json.load(f)
            #Seat A Player A
            self.seat_a_player_a_name_file = settings["seatAPlayerAName"]
            self.seat_a_player_a_deck_file = settings["seatAPlayerADeck"]
            self.seat_a_player_a_record_file = settings["seatAPlayerARecord"]
            self.seat_a_player_a_lifetotal_file = settings["seatAPlayerALifetotal"]

            #Seat A Player B
            self.seat_a_player_b_name_file = settings["seatAPlayerBName"]
            self.seat_a_player_b_deck_file = settings["seatAPlayerBDeck"]
            self.seat_a_player_b_record_file = settings["seatAPlayerBRecord"]
            self.seat_a_player_b_lifetotal_file = settings["seatAPlayerBLifetotal"]

            #Seat B Player A
            self.seat_b_player_a_name_file = settings["seatBPlayerAName"]
            self.seat_b_player_a_deck_file = settings["seatBPlayerADeck"]
            self.seat_b_player_a_record_file = settings["seatBPlayerARecord"]
            self.seat_b_player_a_lifetotal_file = settings["seatBPlayerALifetotal"]

            #Seat B Player B
            self.seat_b_player_b_name_file = settings["seatBPlayerBName"]
            self.seat_b_player_b_deck_file = settings["seatBPlayerBDeck"]
            self.seat_b_player_b_record_file = settings["seatBPlayerBRecord"]
            self.seat_b_player_b_lifetotal_file = settings["seatBPlayerBLifetotal"]

            #Seat C Player A
            self.seat_c_player_a_name_file = settings["seatCPlayerAName"]
            self.seat_c_player_a_deck_file = settings["seatCPlayerADeck"]
            self.seat_c_player_a_record_file = settings["seatCPlayerARecord"]
            self.seat_c_player_a_lifetotal_file = settings["seatCPlayerALifetotal"]

            #Seat C Player B
            self.seat_c_player_b_name_file = settings["seatCPlayerBName"]
            self.seat_c_player_b_deck_file = settings["seatCPlayerBDeck"]
            self.seat_c_player_b_record_file = settings["seatCPlayerBRecord"]
            self.seat_c_player_b_lifetotal_file = settings["seatCPlayerBLifetotal"]

            self.adjustable_lifetotal_left = self.seat_a_player_a_lifetotal_file
            self.adjustable_lifetotal_right = self.seat_a_player_b_lifetotal_file

    def update_player_data(self):

        #Seat A Player A Update
        if self.seat_a_player_a_current_name.get() != "":
            self.write_data_to_file(self.seat_a_player_a_name_file, self.seat_a_player_a_current_name.get())
            self.seat_a_player_a_current_name.set("")

        if self.seat_a_player_a_current_deck.get() != "":
            self.write_data_to_file(self.seat_a_player_a_deck_file, self.seat_a_player_a_current_deck.get())
            self.seat_a_player_a_current_deck.set("")
        
        if self.seat_a_player_a_current_record.get() != "":
            self.write_data_to_file(self.seat_a_player_a_record_file, self.seat_a_player_a_current_record.get())
            self.seat_a_player_a_current_record.set("")

        if self.seat_a_player_a_current_lifetotal.get() != "":
            self.write_data_to_file(self.seat_a_player_a_lifetotal_file, self.seat_a_player_a_current_lifetotal.get())
            self.seat_a_player_a_current_lifetotal.set("")

        #Seat A Player B Update
        if self.seat_a_player_b_current_name.get() != "":
            self.write_data_to_file(self.seat_a_player_b_name_file, self.seat_a_player_b_current_name.get())
            self.seat_a_player_b_current_name.set("")

        if self.seat_a_player_b_current_deck.get() != "":
            self.write_data_to_file(self.seat_a_player_b_deck_file, self.seat_a_player_b_current_deck.get())
            self.seat_a_player_b_current_deck.set("")
        
        if self.seat_a_player_b_current_record.get() != "":
            self.write_data_to_file(self.seat_a_player_b_record_file, self.seat_a_player_b_current_record.get())
            self.seat_a_player_b_current_record.set("")

        if self.seat_a_player_b_current_lifetotal.get() != "":
            self.write_data_to_file(self.seat_a_player_b_lifetotal_file, self.seat_a_player_b_current_lifetotal.get())
            self.seat_a_player_b_current_lifetotal.set("")

        #Seat B Player A Update
        if self.seat_b_player_a_current_name.get() != "":
            self.write_data_to_file(self.seat_b_player_a_name_file, self.seat_b_player_a_current_name.get())
            self.seat_b_player_a_current_name.set("")

        if self.seat_b_player_a_current_deck.get() != "":
            self.write_data_to_file(self.seat_b_player_a_deck_file, self.seat_b_player_a_current_deck.get())
            self.seat_b_player_a_current_deck.set("")
        
        if self.seat_b_player_a_current_record.get() != "":
            self.write_data_to_file(self.seat_b_player_a_record_file, self.seat_b_player_a_current_record.get())
            self.seat_b_player_a_current_record.set("")

        if self.seat_b_player_a_current_lifetotal.get() != "":
            self.write_data_to_file(self.seat_b_player_a_lifetotal_file, self.seat_b_player_a_current_lifetotal.get())
            self.seat_b_player_a_current_lifetotal.set("")

        #Seat B Player B Update
        if self.seat_b_player_b_current_name.get() != "":
            self.write_data_to_file(self.seat_b_player_b_name_file, self.seat_b_player_b_current_name.get())
            self.seat_b_player_b_current_name.set("")

        if self.seat_b_player_b_current_deck.get() != "":
            self.write_data_to_file(self.seat_b_player_b_deck_file, self.seat_b_player_b_current_deck.get())
            self.seat_b_player_b_current_deck.set("")
        
        if self.seat_b_player_b_current_record.get() != "":
            self.write_data_to_file(self.seat_b_player_b_record_file, self.seat_b_player_b_current_record.get())
            self.seat_b_player_b_current_record.set("")

        if self.seat_b_player_b_current_lifetotal.get() != "":
            self.write_data_to_file(self.seat_b_player_b_lifetotal_file, self.seat_b_player_b_current_lifetotal.get())
            self.seat_b_player_b_current_lifetotal.set("")

        #Seat C Player A Update
        if self.seat_c_player_a_current_name.get() != "":
            self.write_data_to_file(self.seat_c_player_a_name_file, self.seat_c_player_a_current_name.get())
            self.seat_c_player_a_current_name.set("")

        if self.seat_c_player_a_current_deck.get() != "":
            self.write_data_to_file(self.seat_c_player_a_deck_file, self.seat_c_player_a_current_deck.get())
            self.seat_c_player_a_current_deck.set("")
        
        if self.seat_c_player_a_current_record.get() != "":
            self.write_data_to_file(self.seat_c_player_a_record_file, self.seat_c_player_a_current_record.get())
            self.seat_c_player_a_current_record.set("")

        if self.seat_c_player_a_current_lifetotal.get() != "":
            self.write_data_to_file(self.seat_c_player_a_lifetotal_file, self.seat_c_player_a_current_lifetotal.get())
            self.seat_c_player_a_current_lifetotal.set("")

        #Seat C Player B Update
        if self.seat_c_player_b_current_name.get() != "":
            self.write_data_to_file(self.seat_c_player_b_name_file, self.seat_c_player_b_current_name.get())
            self.seat_c_player_b_current_name.set("")

        if self.seat_c_player_b_current_deck.get() != "":
            self.write_data_to_file(self.seat_c_player_b_deck_file, self.seat_c_player_b_current_deck.get())
            self.seat_c_player_b_current_deck.set("")
        
        if self.seat_c_player_b_current_record.get() != "":
            self.write_data_to_file(self.seat_c_player_b_record_file, self.seat_c_player_b_current_record.get())
            self.seat_c_player_b_current_record.set("")

        if self.seat_c_player_b_current_lifetotal.get() != "":
            self.write_data_to_file(self.seat_c_player_b_lifetotal_file, self.seat_c_player_b_current_lifetotal.get())
            self.seat_c_player_b_current_lifetotal.set("")

    def change_current_lifetotal_file(self, file_change):
        if file_change == "a":
            self.adjustable_lifetotal_left = self.seat_a_player_a_lifetotal_file
            self.adjustable_lifetotal_right = self.seat_a_player_b_lifetotal_file
            self.current_lifetotal_text.set("Match A")
        
        if file_change == "b":
            self.adjustable_lifetotal_left = self.seat_b_player_a_lifetotal_file
            self.adjustable_lifetotal_right = self.seat_b_player_b_lifetotal_file
            self.current_lifetotal_text.set("Match B")

        if file_change == "c":
            self.adjustable_lifetotal_left = self.seat_c_player_a_lifetotal_file
            self.adjustable_lifetotal_right = self.seat_c_player_b_lifetotal_file
            self.current_lifetotal_text.set("Match C")


    def change_current_lifetotal(self, file_name, amount):
        with open(f"{self.DIRECTORY}{file_name}", "r") as f:
            life_total_value = f.read()
        
        with open(f"{self.DIRECTORY}{file_name}", "w") as f:
            if amount == 20:
                f.write("20")
            else:
                amount = str(int(life_total_value) + amount)
                f.write(amount)

    def write_data_to_file(self, filename, new_value):
        with open(f"{self.DIRECTORY}{filename}", "w") as f:
            f.write(new_value)

root = tk.Tk()
Application(root)
root.mainloop()
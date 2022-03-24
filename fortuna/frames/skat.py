from enum import Enum, unique, auto

import tkinter as tk
from tkinter import ttk

@unique
class Game(Enum):
    DIAMONDS = auto()
    HEARTS = auto()
    SPADES = auto()
    GRAND = auto()
    NULL = auto()


class SkatFrame(ttk.Frame):

    def __init__(self, parent, players):
        super().__init__(master=parent)

        self.frame_bid = BidFrame(self, players)
        self.frame_bid.grid(row=1, column=0, padx=10, pady=10)
        
        self.frame_score = ScoreFrame(self, players)
        self.frame_score.grid(row=0, column=0, columnspan=2, pady=10)

        self.frame_history = HistoryFrame(self)
        self.frame_history.grid(row=1, column=1, padx=10)

class BidFrame(ttk.Frame):
    
    def __init__(self, parent, players):
        super().__init__(master=parent)
        
        self.players = tuple(players)

        # tk variables
        self.var_bid = tk.IntVar()
        self.var_game = tk.IntVar()
        self.var_with = tk.StringVar(value='With')
        
        # Player select row
        ttk.Label(self, text="Bidder").grid(row=0, column=0, pady=10)
        self.combo_player = ttk.Combobox(self, width=10, state='readonly')
        self.combo_player.grid(row=0, column=1, pady=5)
        self.combo_player['values'] = self.players

        # Bid row
        ttk.Label(self, text="Bid").grid(row=1, column=0, pady=10)
        self.e_bid = ttk.Entry(self, width=11).grid(row=1, column=1, pady=5)

        # Game Row
        ttk.Label(self, text="Game").grid(row=1, column=0, pady=5)
        self.combo_game = ttk.Combobox(self, width=10, state='readonly')
        self.combo_game.grid(row=1, column=1, padx=5, pady=10)
        self.combo_game['values'] = tuple([name for name in Game._member_names_])
        self.combo_game.bind('<<ComboboxSelected>>', self.handle_game_change)

        # Announcement row
        ttk.Label(self, text="Declare").grid(row=2, column=0)
        self.combo_declare = ttk.Combobox(self, width=10, state='readonly')
        self.combo_declare.grid(row=2, column=1, padx=5, pady=10)
        self.combo_declare.set('None') 

        # Result row
        ttk.Label(self, text="Result").grid(row=3, column=0, pady=5)
        self.combo_result = ttk.Combobox(self, width=10, state='readonly')
        self.combo_result.grid(row=3, column=1, padx=5, pady=10)
       
        # With/without row
        self.button_with = ttk.Button(
                self,
                textvariable=self.var_with,
                width=7,
                command=self.handle_with_button
                )
        self.button_with.grid(row=4, column=0)
        self.spin_with = ttk.Spinbox(self, from_=1, width=9, state='disabled')
        self.spin_with.grid(row=4, column=1, padx=5, pady=5)

        # Submit row
        self.button_submit = ttk.Button(self, text="Submit", width=15, command=self.handle_submit)
        self.button_submit.grid(row=5, column=0, columnspan=2, pady=5)


    def handle_game_change(self, event):
        suit_games = ('HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS', 'GRAND')

        suit_results = (
                '0 Tricks',
                '0-30 Points',
                '31-60 Points',
                '61-89 Points',
                '90-120 Points',
                '10 Tricks'
                )
        null_results = ('0 Tricks', '1 Trick')

        suit_declarations = ('None', 'Hand', 'Schiender', 'Schwartz', 'Open')
        null_declarations = ('None', 'Hand', 'Open', 'Hand-Open')
        
        # Clear out other comboboxes
        self.combo_result.set('')
        self.combo_declare.set('None')
        game = self.combo_game.get()
        if game in suit_games:
            self.combo_result['values'] = suit_results
            self.combo_declare['values'] = suit_declarations

            with_max = 4 if game == "GRAND" else 11
            self.spin_with.configure(to=with_max, state='normal')
            self.spin_with.set(1)
            self.button_with.configure(state='normal')
            
        else:
            self.combo_result['values'] = null_results
            self.combo_declare['values'] = null_declarations
            self.spin_with.configure(state='disabled')
            self.button_with.configure(state='disabled')

    def handle_with_button(self):
        if self.var_with.get() == 'With':
            self.var_with.set('Without')
        else:
            self.var_with.set('With')
    def handle_submit(self):
        pass

class HistoryFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(master=parent)
        self.grid(row=0, column=0)

        self.history_tree = ttk.Treeview(self, show='headings') 
        self.history_tree['columns'] = ('Bidder', 'Bid', 'Game', 'Declared', 'Result', 'With', 'Scored')

        # Configuring columns
        self.history_tree.column('Bidder', width=100)
        self.history_tree.column('Bid', width=45)
        self.history_tree.column('Game', width=50)
        self.history_tree.column('Declared', width=90)
        self.history_tree.column('Result', width=60)
        self.history_tree.column('With', width=50)
        self.history_tree.column('Scored', width=70)
        
        # Naming column headers
        for col in self.history_tree['columns']:
            self.history_tree.heading(col, text=col)

        self.history_tree.grid(row=0, column=0)


class ScoreFrame(ttk.Frame):
    
    def __init__(self, parent, players):
        super().__init__(master=parent)
        self.grid(row=0, column=0) 
        
        self.players = players
        self.score = {player: tk.IntVar() for player in players}

        # TODO make this work with more than 3 players
        ttk.Label(self, text=players[0]).grid(row=0, column=0, padx=10)
        ttk.Label(self, text=players[1]).grid(row=0, column=1, padx=10)
        ttk.Label(self, text=players[2]).grid(row=0, column=2, padx=10)

        for cnt, player in enumerate(players):
            ttk.Label(self, textvariable=self.score[player]).grid(row=1, column=cnt)

        

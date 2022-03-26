import unittest
import tkinter as tk

from fortuna.frames import skat

class TestHistoryFrame(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
    
    def tearDown(self):
        if self.root:
            self.root.destroy()

    def test_table_header(self):
        history = skat.HistoryFrame(self.root)
        history.grid(row=0, column=0)
        columns = ("Bidder",
            "Bid",
            "Game",
            "Declared",
            "Result",
            "With",
            "Scored",
            )
 
        self.assertTupleEqual(history.history_tree['columns'], columns)

class TestBidFrame(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.players = ['Player 1', 'Player 2', 'Player 3']
        self.test_frame = skat.BidFrame(self.root, self.players)

    def tearDown(self):
        if self.test_frame:
            self.test_frame.destroy()
        if self.root:
            self.root.destroy()

    def test_bidder_values(self):
        self.assertEqual(self.test_frame.combo_player['values'], self.players)

import tkinter as tk
from tkinter import ttk

from frames.skat import SkatFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # root window configuration
        self.title("Fortuna (Skat)")
        self.geometry("700x350")
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)


if __name__ == "__main__":
    players = ["Nate", "Matt", "Josh"]
    app = App()
    frame_skat = SkatFrame(app, players)
    frame_skat.grid(row=0, column=0)

    app.mainloop()

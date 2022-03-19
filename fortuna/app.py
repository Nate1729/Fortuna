import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    

    def __init__(self):
        super().__init__()

        # root window configuration
        self.title('Fortuna')
        self.geometry('800x400')
        self.grid_rowconfigure(0, 
class MainFrame(ttk.Frame):



app = App()
app.mainloop()

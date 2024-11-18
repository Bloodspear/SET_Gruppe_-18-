import tkinter as tk
from enheter import Enheter
from enhetskontroll import Enhetskontroll

class Homepage:
    def __init__(self, test):
        self.test = test
        self.test.title("Home")
        self.create_home()

    def create_home(self):
        # Venstre del
        self.left_frame = tk.Frame(self.test, bg='grey65')
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Høyre del
        self.right_frame = tk.Frame(self.test, bg='white')

        # Knapper i høyre del
        self.enheter = Enheter(self)
        self.enheter.create_buttons(self.left_frame)

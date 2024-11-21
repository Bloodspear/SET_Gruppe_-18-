import tkinter as tk
from enheter import Enheter

class Hjemmeside:
    def __init__(self, root):
        self.root = root
        self.root.title("Home")
        self.enheter = Enheter(self.root)
        self.create_home()

    def create_home(self):
        self.left_frame = tk.Frame(self.root, bg='grey65')
        self.left_frame.pack(side="left", fill="both", expand=True)
        header_label = tk.Label(self.left_frame, text="Smart Enheter", font=("Helvetica", 20), bg='grey65')
        header_label.pack(pady=20)
        self.legg_til_knapp = tk.Button(self.left_frame, text="Legg til enhet", bg='white', activebackground='grey',
                                    command=self.enheter.legg_til_knapp_klikk)
        self.legg_til_knapp.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

import tkinter as tk
from enhetskontroll import Enhetskontroll

class Enheter:
    def __init__(self, root):
        self.root = root
        self.enhet_knapp = []
        self.right_frame = tk.Frame(self.root, bg='grey85')
        self.right_frame.pack(side="right", fill="both", expand=True)
        self.right_frame.pack_forget()

    def legg_til_knapp_klikk(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Legg til enhet")
        add_window.geometry("400x300")
        label = tk.Label(add_window, text="Velg kategori og navn", font=("Helvetica", 16))
        label.pack(pady=10)
        knapp_frame = tk.Frame(add_window)
        knapp_frame.pack(pady=10)
        self.name_input = tk.Entry(add_window, font=("Helvetica", 12))
        self.name_input.pack(pady=20)
        self.submit_knapp = tk.Button(add_window, text="Legg til enhet", command=lambda: self.legg_til_enhet(add_window))
        self.submit_knapp.pack()

        kategorier = ["Varmeovn", "Lys", "Stikkontakt"]
        for i, kategori in enumerate(kategorier):
            knapp = tk.Button(knapp_frame, text=kategori, command=lambda c=kategori: self.set_kategori(c))
            knapp.grid(row=0, column=i, padx=5)

    def set_kategori(self, kategori):
        self.valgt_kategori = kategori
        self.name_input.focus_set()

    def legg_til_enhet(self, add_window):
        if len(self.enhet_knapp) >= 6:
            print("Maks 6 enheter tillatt.")
            add_window.destroy()
            return

        name = self.name_input.get()

        # sjekker at både kategori og navn er satt
        if not name:
            print("enheten må ha et navn")
            return
        if not hasattr(self, 'valgt_kategori') or not self.valgt_kategori:
            print("velg en kategori")
            return

        print(f"legger enhet i {self.valgt_kategori}, Navn - {name}")

        # Legger enheten
        add_window.destroy()
        enhetsknapp_text = f"{self.valgt_kategori} ({name})"

        # Setter knapp
        enhetsknapp = tk.Button(self.root, text=enhetsknapp_text, bg='white', activebackground='grey',
                                  wraplength=100, width=10, height=4)
        enhetsknapp.config(
            command=lambda c=self.valgt_kategori, n=name, b=enhetsknapp: self.enhetsklikk(c, n, b))

        # legger knappen i listen med enhetene
        self.enhet_knapp.append(enhetsknapp)
        self.enhetsplassering()

    def enhetsplassering(self):
        for index, knapp in enumerate(self.enhet_knapp):
            knapp_x = 100 + (index % 2) * 200
            knapp_y = 150 + (index // 2) * 150
            knapp.place(x=knapp_x, y=knapp_y, width=100, height=100)

    def enhetsklikk(self, kategori, name, enhetsknapp):
        # Tømmer høyre ramme
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        # Opprett en ny høyre ramme
        Enhetskontroll(self.right_frame, kategori, name, enhetsknapp, self.enhet_knapp,
                       self.enhetsplassering)

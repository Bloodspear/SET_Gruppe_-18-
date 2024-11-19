import tkinter as tk

class Enhetskontroll:
    def __init__(self, right_frame, kategori, name, enhetsknapp, enhetsknapper, enhetsplassering):
        self.right_frame = right_frame
        self.kategori = kategori
        self.name = name
        self.enhetsknapp = enhetsknapp
        self.enhetsknapper = enhetsknapper
        self.enhetsplassering = enhetsplassering
        self.show_right_frame()

    def show_right_frame(self):
        # Tømmer høyre frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        
        # Viser høyre frame
        self.right_frame.pack(side="right", fill="both", expand=True)
        
        # Legger til tittel
        title_label = tk.Label(self.right_frame, text=f"{self.kategori} - {self.name}", bg='white', font=("Helvetica", 20))
        title_label.place(relx=0.5, y=20, anchor=tk.CENTER)
        
        # Legger til høyre frame basert på kategori
        if self.kategori == "Varmeovn":
            self.varmeovn_funskjoner()
        elif self.kategori == "Lys":
            self.lys_funskjoner()
        elif self.kategori == "Stikkontakt":
            self.stikkontakt_funskjoner()
        
        # Legger til fjern enhet-knapp
        fjern_enhet = tk.Button(self.right_frame, text="Fjern enhet", bg='red', fg='white', command=self.remove_device)
        fjern_enhet.place(relx=0.5, y=200, anchor=tk.CENTER)

    def varmeovn_funskjoner(self):
        on_off_button = tk.Button(self.right_frame, text="På/Av", command=self.on_off_bryter, bg='tomato')
        on_off_button.place(relx=0.5, y=60, width=100, height=30, anchor=tk.CENTER)
        
        self.temperatur = 22
        self.temp_label = tk.Label(self.right_frame, text=f"Temperatur: {self.temperatur} °C", bg='white')
        self.temp_label.place(relx=0.5, y=120, anchor=tk.CENTER)
        
        increase_knapp = tk.Button(self.right_frame, text="+", command=self.increase_temp, bg='tomato')
        increase_knapp.place(relx=0.55, y=160, width=25, height=25, anchor=tk.CENTER)
        
        decrease_knapp = tk.Button(self.right_frame, text="-", command=self.decrease_temp, bg='cyan')
        decrease_knapp.place(relx=0.45, y=160, width=25, height=25, anchor=tk.CENTER)

    def lys_funskjoner(self):
        on_off_button = tk.Button(self.right_frame, text="På/Av", command=self.on_off_bryter, bg='tomato')
        on_off_button.place(relx=0.5, y=60, width=100, height=30, anchor=tk.CENTER)
        
        farge_knapp = tk.Button(self.right_frame, text="Endre farge", command=self.endre_lysfarge, bg='yellow')
        farge_knapp.place(relx=0.5, y=120, width=100, height=30, anchor=tk.CENTER)

    def stikkontakt_funskjoner(self):
        on_off_button = tk.Button(self.right_frame, text="På/Av", command=self.on_off_bryter, bg='tomato')
        on_off_button.place(relx=0.5, y=60, width=100, height=30, anchor=tk.CENTER)

    def remove_device(self):
        self.enhetsknapp.destroy()
        self.enhetsknapper.remove(self.enhetsknapp)
        self.enhetsplassering()
        
        # Tømmer høyre frame og pakker den.
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.right_frame.pack_forget()

    def on_off_bryter(self):
        print("Av og på Knapp trykket")

        #øker temperatur
    def increase_temp(self):
        if self.temperatur < 40:
            self.temperatur += 1
            self.temp_label.config(text=f"Temperatur: {self.temperatur} °C")

        #senker temperatur
    def decrease_temp(self):
        if self.temperatur > 15:
            self.temperatur -= 1
            self.temp_label.config(text=f"Temperatur: {self.temperatur} °C")

    def endre_lysfarge(self):
        print("Endre lysfarge")

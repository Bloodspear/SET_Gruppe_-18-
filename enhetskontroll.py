class Enhetskontroll:
    def init(self, homepage):
        self.homepage = homepage

    # temperatur +
    def increase_temp(self):
        self.temperature += 1
        self.temp_label.config(text=f"Grader: {self.temperature} °C")

    # temperatur -
    def decrease_temp(self):
        self.temperature -= 1
        self.temp_label.config(text=f"Grader: {self.temperature} °C")

    # lys av/på
    def toggle_light(self):
        if self.light_status == "Av":
            self.light_status = "På"
            self.farge = "gold"
        else:
            self.light_status = "Av"
            self.farge = "gray40"
        self.light_label.config(text=f"Lys: {self.light_status}")
        self.light_button.config(bg=self.farge)
    
    def show_right_frame(self, device_name, initial_temp):
        # viser høyre del
        if not self.right_frame.winfo_ismapped():
            self.right_frame.pack(side="right", fill="both", expand=True)

        # tømmer høyre del hver gang den vises
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # overskrift med enhetsnavn
        title_label = tk.Label(self.right_frame, text=device_name, bg='white', font=("Helvetica", 20))
        title_label.place(relx=0.5, y=20, anchor=tk.CENTER)

        # temperature
        self.temperature = initial_temp  # Hold styr på temperaturen for denne enheten
        self.temp_label = tk.Label(self.right_frame, text=f"Grader: {self.temperature} °C", bg='white')
        self.temp_label.place(relx=0.5, y=60, anchor=tk.CENTER)

        # knapper for temperatur
        self.enhetskontroll = Enhetskontroll(self)
        increase_button = tk.Button(self.right_frame, text="+", command=self.enhetskontroll.increase_temp, bg='tomato')
        increase_button.place(relx=0.55, y=100, width=25, height=25, anchor=tk.CENTER)

        decrease_button = tk.Button(self.right_frame, text="-", command=self.enhetskontroll.decrease_temp, bg='cyan')
        decrease_button.place(relx=0.45, y=100, width=25, height=25, anchor=tk.CENTER)

        # Lys status og knapp
        self.farge = "gray40"
        self.light_status = "Av"
        self.light_label = tk.Label(self.right_frame, text=f"Lys: {self.light_status}")
        self.light_label.place(relx=0.5, y=170, anchor=tk.CENTER)

        self.light_button = tk.Button(self.right_frame, text="Endre lys", command=self.enhetskontroll.toggle_light, bg=self.farge)
        self.light_button.place(relx=0.5, y=210, width=100, height=50, anchor=tk.CENTER)

        # Produktinformasjon
        info_label = tk.Label(self.right_frame, text="Produktinformasjon:", font=("Helvetica", 12))
        info_label.place(relx=0.5, y=280, anchor=tk.CENTER)

        produktinfo_tekst = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum elementum risus enim, "
            "ut condimentum sapien euismod vitae. Aenean eleifend cursus iaculis. Praesent pellentesque "
            "tempor odio, eget convallis magna ornare quis. Donec interdum ut orci a euismod. Donec in ")

        infopanel = tk.Label(self.right_frame, text=produktinfo_tekst, bg="white", wraplength=300, justify="left")
        infopanel.place(relx=0.5, y=350, anchor=tk.CENTER)

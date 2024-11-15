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

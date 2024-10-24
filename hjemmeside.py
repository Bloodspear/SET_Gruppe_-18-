import tkinter
import tkinter as tk

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
        pc = tk.Button(self.left_frame, text="PC", bg='white', activebackground='grey', command=self.pc_clicked)
        pc.place(x=50, y=50, width=100, height=100)
        tablet = tk.Button(self.left_frame, text="Tablet", bg='white', activebackground='grey', command=self.tablet_clicked)
        tablet.place(x=200, y=50, width=100, height=100)
        kjoleskap = tk.Button(self.left_frame, text="Kjøleskap", bg='white', activebackground='grey', command=self.kjoleskap_clicked)
        kjoleskap.place(x=50, y=200, width=100, height=100)
        printer = tk.Button(self.left_frame, text="Printer", bg='white', activebackground='grey', command=self.printer_clicked)
        printer.place(x=200, y=200, width=100, height=100)
        kamera = tk.Button(self.left_frame, text="Kamera", bg='white', activebackground='grey', command=self.kamera_clicked)
        kamera.place(x=50, y=350, width=100, height=100)
        vifte = tk.Button(self.left_frame, text="Vifte", bg='white', activebackground='grey', command=self.vifte_clicked)
        vifte.place(x=200, y=350, width=100, height=100)

    # Funksjoner for knapper
    def pc_clicked(self):
        self.show_right_frame("PC", 25)

    def tablet_clicked(self):
        self.show_right_frame("Tablet", 20)

    def kjoleskap_clicked(self):
        self.show_right_frame("Kjøleskap", 22)

    def printer_clicked(self):
        self.show_right_frame("Printer", 18)

    def kamera_clicked(self):
        self.show_right_frame("Kamera", 21)

    def vifte_clicked(self):
        self.show_right_frame("Vifte", 24)

    # Funksjon for å vise høyre del og elementer i høyre del
    def show_right_frame(self, device_name, initial_temp):
        # viser høyre del
        if not self.right_frame.winfo_ismapped():
            self.right_frame.pack(side="right", fill="both", expand=True)

        # tømmer høyre del hver gang den vises
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # overskrift med enhetsnavn
        title_label = tk.Label(self.right_frame, text=device_name, bg='white', font=("Helvetica", 20))
        title_label.place(relx=0.5, y=20, anchor=tkinter.CENTER)

        # temperature
        self.temperature = initial_temp  # Hold styr på temperaturen for denne enheten
        self.temp_label = tk.Label(self.right_frame, text=f"Grader: {self.temperature} °C", bg='white')
        self.temp_label.place(relx=0.5, y=60, anchor=tkinter.CENTER)

        # knapper for temperatur
        increase_button = tk.Button(self.right_frame, text="+", command=self.increase_temp, bg='tomato')
        increase_button.place(relx=0.55, y=100, width=25, height=25,anchor=tkinter.CENTER)

        decrease_button = tk.Button(self.right_frame, text="-", command=self.decrease_temp, bg='cyan')
        decrease_button.place(relx=0.45, y=100, width=25, height=25,anchor=tkinter.CENTER)

        # Lys status og knapp
        self.light_status = "Av"
        self.light_label = tk.Label(self.right_frame, text=f"Lys: {self.light_status}")
        self.light_label.place(relx=0.5, y=170, anchor=tkinter.CENTER)

        self.light_button = tk.Button(self.right_frame, text="Endre lys", command=self.toggle_light)
        self.light_button.place(relx=0.5, y=210, width=100, height=50, anchor=tkinter.CENTER)

        #Produktinformasjon
        info_label = tk.Label(self.right_frame, text="Produktinformasjon:", font=("Helvetica", 12))
        info_label.place(relx=0.5, y=280, anchor=tkinter.CENTER)

        produktinfo_tekst = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum elementum risus enim, "
            "ut condimentum sapien euismod vitae. Aenean eleifend cursus iaculis. Praesent pellentesque "
            "tempor odio, eget convallis magna ornare quis. Donec interdum ut orci a euismod. Donec in ")

        infopanel = tk.Label(self.right_frame, text=produktinfo_tekst, bg="white",wraplength=300,justify="left")
        infopanel.place(relx=0.5, y=350, anchor=tkinter.CENTER)




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
        else:
            self.light_status = "Av"
        self.light_label.config(text=f"Lys: {self.light_status}")


# starter hovedvindu
test = tk.Tk()
app = Homepage(test)
test.geometry("800x800")  #størrelse på vinduet
test.mainloop()

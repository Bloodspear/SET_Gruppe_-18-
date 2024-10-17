import tkinter as tk


class Homepage:
    def __init__(self, test):
        self.test = test
        self.test.title("Home")
        self.create_home()

    def create_home(self):
        # Venstre ramme (blå) som fyller hele vinduet i starten
        self.left_frame = tk.Frame(self.test, bg='lightblue')
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Høyre ramme (hvit) som er skjult i starten
        self.right_frame = tk.Frame(self.test, bg='white')

        # Knapper i den lyseblå rammen
        button1 = tk.Button(self.left_frame, text="Button 1",bg='red',activebackground='green', command=self.button1_clicked)
        button1.place(x=50, y=50, width=100, height=100)
        button2 = tk.Button(self.left_frame, text="Button 2",bg='red',activebackground='green', command=self.button2_clicked)
        button2.place(x=200, y=50, width=100, height=100)

    def button1_clicked(self):
        self.show_right_frame("You clicked Button 1")

    def button2_clicked(self):
        self.show_right_frame("You clicked Button 2")

    def show_right_frame(self, text):
        # Hvis høyre ramme ikke er vist, pakk den ut
        if not self.right_frame.winfo_ismapped():
            self.right_frame.pack(side="right", fill="both", expand=True)

        # Fjern eksisterende widgets fra høyre ramme (om noen)
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        # Legg til en label i høyre ramme med tekst fra knappetrykket
        label = tk.Label(self.right_frame, text=text, bg='white')
        label.pack(pady=20)


# Opprett hovedvinduet
test = tk.Tk()
app = Homepage(test)
test.geometry("800x800")  # Sett størrelse på vinduet
test.mainloop()
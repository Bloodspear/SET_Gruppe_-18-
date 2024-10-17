import tkinter as tk


class Homepage:
    def __init__(self, test):
        self.test = test
        self.test.title("Home")
        self.create_home()

    def create_home(self):
        homepage_frame = tk.Frame(self.test, bg='lightblue')
        homepage_frame.pack(side="left", fill="both", expand=True)

test = tk.Tk()
app = Homepage(test)
test.geometry("800x800")
test.mainloop()
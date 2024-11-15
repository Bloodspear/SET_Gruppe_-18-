import tkinter as tk
from hjemmeside import Homepage

# Starter hovedvindu
test = tk.Tk()
app = Homepage(test)
test.geometry("800x800")  # Størrelse på vinduet
test.mainloop()
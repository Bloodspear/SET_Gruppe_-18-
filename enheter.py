import tkinter as tk

class Enheter(object):
	def __init__(self,homepage):
		self.homepage=Homepage
		
	def create_buttons(self,frame):
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
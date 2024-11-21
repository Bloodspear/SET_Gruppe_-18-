import unittest
import tkinter as tk
from enheter import Enheter
from enhetskontroll import Enhetskontroll


class TestPrototype(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()

# tester til legg til enhet funksjonen
    def test_legg_til_enhet(self):

        enheter = Enheter(self.root)
        enheter.valgt_kategori = "Lys"
        enheter.name_input = tk.Entry(self.root)
        enheter.name_input.insert(0, "Stue Lys")


        add_window = tk.Toplevel(self.root)
        enheter.legg_til_enhet(add_window)

        self.assertEqual(len(enheter.enhet_knapp), 1)
        self.assertEqual(enheter.enhet_knapp[0]['text'], "Lys (Stue Lys)")

# sjekker at man ikke kan legge til flere enn 6 enheter.
    def test_legg_til_enheter_max(self):

        enheter = Enheter(self.root)
        enheter.valgt_kategori = "Varmeovn"


        for i in range(6):
            enheter.name_input = tk.Entry(self.root)
            enheter.name_input.insert(0, f"Enhet {i}")
            add_window = tk.Toplevel(self.root)
            enheter.legg_til_enhet(add_window)

        self.assertEqual(len(enheter.enhet_knapp), 6)


        add_window = tk.Toplevel(self.root)
        enheter.name_input.insert(0, "Ekstra Enhet")
        with self.assertRaises(Exception):
            enheter.legg_til_enhet(add_window)

# sjekker om den increaser temperatur
    def test_increase_temp(self):
        right_frame = tk.Frame(self.root)
        enhetskontroll = Enhetskontroll(right_frame, "Varmeovn", "Stue", None, [], None)
        initial_temp = enhetskontroll.temperatur
        enhetskontroll.increase_temp()
        self.assertEqual(enhetskontroll.temperatur, initial_temp + 1)

# sjekker om den synker temperatur
    def test_decrease_temp(self):
        right_frame = tk.Frame(self.root)
        enhetskontroll = Enhetskontroll(right_frame, "Varmeovn", "Stue", None, [], None)
        enhetskontroll.temperatur = 20
        enhetskontroll.decrease_temp()
        self.assertEqual(enhetskontroll.temperatur, 19)

    def tearDown(self):
        self.root.destroy()

import tkinter as tk
import random
import threading

class Auto:
    def __init__(self):
        self.ocupado = False

class Estacionamiento:
    def __init__(self, size):
        self.size = size
        self.estacionamiento = [Auto() for _ in range(size)]
        self.gui = None
        self.add_timer = None
        self.remove_timer = None

    def create_gui(self, root):
        self.gui = tk.Frame(root)
        self.gui.grid(row=0, column=0)
        self.update_gui()

    def update_gui(self):
        for i, auto in enumerate(self.estacionamiento):
            color = "red" if auto.ocupado else "green"
            square = tk.Canvas(self.gui, width=40, height=40, bg=color)
            square.grid(row=i // 6, column=i % 6, padx=5, pady=5)

    def add_auto(self):
        empty_spots = [i for i, auto in enumerate(self.estacionamiento) if not auto.ocupado]
        if empty_spots:
            spot = random.choice(empty_spots)
            self.estacionamiento[spot].ocupado = True
            self.update_gui()
            print("Un auto ha ingresado al estacionamiento.")

    def remove_auto(self):
        occupied_spots = [i for i, auto in enumerate(self.estacionamiento) if auto.ocupado]
        if occupied_spots:
            spot = random.choice(occupied_spots)
            self.estacionamiento[spot].ocupado = False
            self.update_gui()
            print("Un auto ha salido del estacionamiento.")

    def change_add_timer(self, frequency):
        self.add_timer.cancel()
        self.add_timer = threading.Timer(frequency, self.change_add_timer, [frequency])
        self.add_timer.start()
        self.add_auto()

    def change_remove_timer(self, frequency):
        self.remove_timer.cancel()
        self.remove_timer = threading.Timer(frequency, self.change_remove_timer, [frequency])
        self.remove_timer.start()
        self.remove_auto()

    def start(self):
        self.add_timer = threading.Timer(1, self.change_add_timer, [1])
        self.remove_timer = threading.Timer(1, self.change_remove_timer, [1])
        self.add_timer.start()
        self.remove_timer.start()

def close_program(root, estacionamiento):
    if estacionamiento.add_timer:
        estacionamiento.add_timer.cancel()
    if estacionamiento.remove_timer:
        estacionamiento.remove_timer.cancel()
    root.destroy()

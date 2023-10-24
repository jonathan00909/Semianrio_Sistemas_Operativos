import tkinter as tk
from estacionamiento import Estacionamiento, close_program

def main():
    root = tk.Tk()
    root.title("Estacionamiento")

    size = 12
    estacionamiento = Estacionamiento(size)
    estacionamiento.create_gui(root)
    estacionamiento.start()

    add_frequency_label = tk.Label(root, text="Frecuencia para añadir autos (segundos):")
    add_frequency_label.grid(row=1, column=0)
    add_frequency = tk.Entry(root)
    add_frequency.insert(0, "1")
    add_frequency.grid(row=1, column=1)
    add_button = tk.Button(root, text="Cambiar Frecuencia de Entrada", command=lambda: estacionamiento.change_add_timer(float(add_frequency.get())))
    add_button.grid(row=1, column=2)

    remove_frequency_label = tk.Label(root, text="Frecuencia para retirar autos (segundos):")
    remove_frequency_label.grid(row=2, column=0)
    remove_frequency = tk.Entry(root)
    remove_frequency.insert(0, "1")
    remove_frequency.grid(row=2, column=1)
    remove_button = tk.Button(root, text="Cambiar Frecuencia de Salida", command=lambda: estacionamiento.change_remove_timer(float(remove_frequency.get())))
    remove_button.grid(row=2, column=2)

    close_button = tk.Button(root, text="Cerrar", command=lambda: close_program(root, estacionamiento))
    close_button.grid(row=3, column=0, columnspan=3)

    root.mainloop()

if __name__ == "__main__":
    main()

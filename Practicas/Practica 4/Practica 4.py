import queue
import os

# Ruta completa del archivo "procesos.txt"
ruta_archivo = r'D:\Practica 3\procesos.txt'

# Verifica si el archivo existe en la ruta especificada
if not os.path.isfile(ruta_archivo):
    print("El archivo 'procesos.txt' no se encuentra en la ubicación especificada.")
    exit()

# Función para agregar un nuevo proceso al archivo
def agregar_proceso():
    nombre = input("Nombre del proceso: ")

    # Validación del tiempo como número entero
    while True:
        tiempo = input("Tiempo del proceso (entero): ")
        if tiempo.isdigit():
            break
        else:
            print("El tiempo debe ser un número entero.")

    # Validación de la prioridad como número entero
    while True:
        prioridad = input("Prioridad del proceso (entero): ")
        if prioridad.isdigit():
            break
        else:
            print("La prioridad debe ser un número entero.")

    posicion = input("¿Deseas agregar al principio o al final? (P = Principio, F = Final): ").strip().lower()

    if posicion == 'p':
        # Insertar al principio del archivo
        with open(ruta_archivo, "r") as file:
            procesos = [line.strip() for line in file.readlines()]
        with open(ruta_archivo, "w") as file:
            file.write(f"{nombre}, {tiempo}, {prioridad}\n")
            for proceso in procesos:
                file.write(proceso + "\n")
    else:
        # Agregar al final del archivo
        with open(ruta_archivo, "a") as file:
            file.write(f"{nombre}, {tiempo}, {prioridad}\n")

# Función para cargar los procesos desde el archivo y crear las colas
def cargar_procesos_y_colas():
    with open(ruta_archivo, "r") as file:
        procesos = [line.strip().split(", ") for line in file.readlines()]
    procesos = [(nombre, int(tiempo), int(prioridad)) for nombre, tiempo, prioridad in procesos]

    cola_listos_rr = queue.Queue()
    cola_listos_sjf = []
    cola_listos_fifo = queue.Queue()
    cola_listos_prioridades = queue.PriorityQueue()

    for proceso in procesos:
        cola_listos_rr.put(proceso)
        cola_listos_sjf.append(proceso)
        cola_listos_fifo.put(proceso)
        cola_listos_prioridades.put((proceso[2], proceso))

    return procesos, cola_listos_rr, cola_listos_sjf, cola_listos_fifo, cola_listos_prioridades

# Crear colas (queues) y cargar los procesos al inicio
procesos, cola_listos_rr, cola_listos_sjf, cola_listos_fifo, cola_listos_prioridades = cargar_procesos_y_colas()

def simular_round_robin():
    lapso_rr = 3  # Cambia este valor según tus necesidades
    tiempo_total_rr = 0

    print("Simulación de Round Robin:")
    while not cola_listos_rr.empty():
        proceso_actual = cola_listos_rr.get()
        nombre, tiempo_restante, prioridad = proceso_actual
        
        # Verifica si el tiempo restante es mayor que cero antes de ejecutar el proceso
        if tiempo_restante > 0:
            ejecucion = min(lapso_rr, tiempo_restante)
            tiempo_total_rr += ejecucion
            tiempo_restante -= ejecucion

            # Muestra el resultado de la ejecución del proceso actual en Round Robin
            print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_rr}")

            if tiempo_restante > 0:
                # Si el proceso aún tiene tiempo restante, vuelve a agregarlo a la cola de listos
                cola_listos_rr.put((nombre, tiempo_restante, prioridad))

def simular_sjf():
    cola_listos_sjf.sort(key=lambda x: x[1])  # Ordena la cola por tiempo de ejecución
    tiempo_total_sjf = 0

    print("\nSimulación de Shortest Job First:")
    while cola_listos_sjf:
        proceso_actual = cola_listos_sjf.pop(0)
        nombre, tiempo_restante, prioridad = proceso_actual
        tiempo_total_sjf += tiempo_restante

        # Muestra el resultado de la ejecución del proceso actual en SJF
        print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_sjf}")

def simular_fifo():
    tiempo_total_fifo = 0

    print("\nSimulación de First In, First Out:")
    while not cola_listos_fifo.empty():
        proceso_actual = cola_listos_fifo.get()
        nombre, tiempo_restante, prioridad = proceso_actual
        tiempo_total_fifo += tiempo_restante

        # Muestra el resultado de la ejecución del proceso actual en FIFO
        print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_fifo}")

def simular_prioridades():
    tiempo_total_prioridades = 0

    print("\nSimulación de Prioridades:")
    while not cola_listos_prioridades.empty():
        proceso_actual = cola_listos_prioridades.get()[1]  # Obtiene el proceso de la cola
        nombre, tiempo_restante, prioridad = proceso_actual
        tiempo_total_prioridades += tiempo_restante

        # Muestra el resultado de la ejecución del proceso actual en Prioridades
        print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_prioridades}")

while True:
    print("\nSelecciona una opción:")
    print("1. Simular Round Robin")
    print("2. Simular Shortest Job First (SJF)")
    print("3. Simular First In, First Out (FIFO)")
    print("4. Simular Prioridades")
    print("5. Realizar todas las simulaciones")
    print("6. Agregar un nuevo proceso")
    print("7. Salir")
    
    opcion = input("Elije una opción: ")

    if opcion == "1":
        procesos, cola_listos_rr, _, _, _ = cargar_procesos_y_colas()
        simular_round_robin()
    elif opcion == "2":
        procesos, _, cola_listos_sjf, _, _ = cargar_procesos_y_colas()
        simular_sjf()
    elif opcion == "3":
        procesos, _, _, cola_listos_fifo, _ = cargar_procesos_y_colas()
        simular_fifo()
    elif opcion == "4":
        procesos, _, _, _, cola_listos_prioridades = cargar_procesos_y_colas()
        simular_prioridades()
    elif opcion == "5":
        procesos, cola_listos_rr, cola_listos_sjf, cola_listos_fifo, cola_listos_prioridades = cargar_procesos_y_colas()
        simular_round_robin()
        simular_sjf()
        simular_fifo()
        simular_prioridades()
    elif opcion == "6":
        agregar_proceso()
        procesos, cola_listos_rr, cola_listos_sjf, cola_listos_fifo, cola_listos_prioridades = cargar_procesos_y_colas()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida (1-7).")

print("\nTodos los procesos han terminado.")

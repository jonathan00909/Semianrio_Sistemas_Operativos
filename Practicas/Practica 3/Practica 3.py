import queue
import os

# Ruta completa del archivo "procesos.txt"
ruta_archivo = r''

# Verifica si el archivo existe en la ruta especificada
if not os.path.isfile(ruta_archivo):
    print("El archivo 'procesos.txt' no se encuentra en la ubicación especificada.")
    exit()

# Lee el archivo procesos.txt y crea una lista de procesos
with open(ruta_archivo, "r") as file:
    procesos = [line.strip().split(", ") for line in file.readlines()]

# Convierte los tiempos y prioridades a enteros
procesos = [(nombre, int(tiempo), int(prioridad)) for nombre, tiempo, prioridad in procesos]

# Crea una cola (queue) para los procesos listos para Round Robin
cola_listos_rr = queue.Queue()

# Crea una cola (queue) para los procesos listos para SJF
cola_listos_sjf = []

# Crea una cola (queue) para los procesos listos para FIFO
cola_listos_fifo = queue.Queue()

# Crea una cola (queue) para los procesos listos para Prioridades
cola_listos_prioridades = queue.PriorityQueue()

# Agrega los procesos a las colas de listos
for proceso in procesos:
    cola_listos_rr.put(proceso)
    cola_listos_sjf.append(proceso)
    cola_listos_fifo.put(proceso)
    cola_listos_prioridades.put((proceso[2], proceso))  # Agrega el proceso con su prioridad como clave

# Simula el algoritmo Round Robin
lapso_rr = 2  # Cambia este valor según tus necesidades
tiempo_total_rr = 0

print("Simulación de Round Robin:")
while not cola_listos_rr.empty():
    proceso_actual = cola_listos_rr.get()
    nombre, tiempo_restante, prioridad = proceso_actual
    tiempo_total_rr += min(lapso_rr, tiempo_restante)
    tiempo_restante -= lapso_rr

    if tiempo_restante > 0:
        # Si el proceso aún tiene tiempo restante, vuelve a agregarlo a la cola de listos
        cola_listos_rr.put((nombre, tiempo_restante, prioridad))
    
    # Muestra el resultado de la ejecución del proceso actual en Round Robin
    print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_rr}")

# Simula el algoritmo SJF
cola_listos_sjf.sort(key=lambda x: x[1])  # Ordena la cola por tiempo de ejecución
tiempo_total_sjf = 0

print("\nSimulación de Shortest Job First:")
while cola_listos_sjf:
    proceso_actual = cola_listos_sjf.pop(0)
    nombre, tiempo_restante, prioridad = proceso_actual
    tiempo_total_sjf += tiempo_restante

    # Muestra el resultado de la ejecución del proceso actual en SJF
    print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_sjf}")

# Simula el algoritmo FIFO
tiempo_total_fifo = 0

print("\nSimulación de First In, First Out:")
while not cola_listos_fifo.empty():
    proceso_actual = cola_listos_fifo.get()
    nombre, tiempo_restante, prioridad = proceso_actual
    tiempo_total_fifo += tiempo_restante

    # Muestra el resultado de la ejecución del proceso actual en FIFO
    print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_fifo}")

# Simula el algoritmo de Prioridades
tiempo_total_prioridades = 0

print("\nSimulación de Prioridades:")
while not cola_listos_prioridades.empty():
    proceso_actual = cola_listos_prioridades.get()[1]  # Obtiene el proceso de la cola
    nombre, tiempo_restante, prioridad = proceso_actual
    tiempo_total_prioridades += tiempo_restante

    # Muestra el resultado de la ejecución del proceso actual en Prioridades
    print(f"Proceso: {nombre}, Tiempo Restante: {tiempo_restante}, Tiempo Total: {tiempo_total_prioridades}")

print("\nTodos los procesos han terminado.")

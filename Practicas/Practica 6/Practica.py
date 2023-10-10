import os

# Función para leer los datos del archivo "archivos.txt"
def leer_archivos():
    archivos = []
    try:
        with open('C:\\Users\\jonat\\OneDrive\\Escritorio\\Practica 6\\archivos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, tamaño = linea.strip().split(',')
                archivos.append((nombre, int(tamaño[:-2])))  # Elimina "kb" y convierte el tamaño a int
    except FileNotFoundError:
        print("El archivo 'archivos.txt' no se encontró.")
    return archivos

# Función para leer la memoria disponible del archivo "memoria.txt"
def leer_memoria():
    memoria = []
    try:
        with open('C:\\Users\\jonat\\OneDrive\\Escritorio\\Practica 6\\memoria.txt', 'r') as archivo:
            for linea in archivo:
                memoria.append(int(linea))
    except FileNotFoundError:
        print("El archivo 'memoria.txt' no se encontró.")
    return memoria

# Función para agregar memoria al archivo de memoria
def agregar_memoria(memoria_disponible):
    try:
        nueva_memoria = int(input("Ingrese la cantidad de memoria a agregar (en KB): "))
        guardar = input("¿Desea guardar esta memoria al inicio (I) o al final (F) del archivo de memoria? ").strip().lower()
        
        if guardar == 'i':
            memoria_disponible.insert(0, nueva_memoria)
        elif guardar == 'f':
            memoria_disponible.append(nueva_memoria)
        else:
            print("Opción no válida. No se agregó la memoria.")

        with open('C:\\Users\\jonat\\OneDrive\\Escritorio\\Practica 6\\memoria.txt', 'w') as archivo:
            for mem in memoria_disponible:
                archivo.write(f"{mem}\n")
        print(f"Se agregaron {nueva_memoria}KB de memoria al archivo de memoria.")

    except ValueError:
        print("Por favor, ingrese un valor numérico válido para la memoria.")

# Función para agregar un proceso a la lista de archivos
def agregar_proceso(archivos):
    try:
        nombre_proceso = input("Ingrese el nombre del proceso: ")
        tamaño_proceso = int(input("Ingrese el tamaño del proceso (en KB): "))
        archivos.append((nombre_proceso, tamaño_proceso))
        print(f"Se agregó el proceso '{nombre_proceso}' de {tamaño_proceso}KB a la lista de archivos.")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido para el tamaño del proceso.")



# Función para realizar la asignación de memoria con el algoritmo de primer ajuste
def primer_ajuste(archivos, memoria_disponible):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    
    for nombre_archivo, tamano_archivo in archivos:
        asignado = False
        for i in range(len(memoria_disponible)):
            if memoria_disponible[i] >= tamano_archivo:
                memoria_disponible[i] -= tamano_archivo
                memoria_usada[i] += tamano_archivo  # Actualizar la memoria usada en esta partición
                print(f"El archivo '{nombre_archivo}' de {tamano_archivo}KB se asignó a la partición {i + 1} (Primer ajuste).")
                asignado = True
                break
        if not asignado:
            print(f"No se pudo asignar el archivo '{nombre_archivo}' de {tamano_archivo}KB a ninguna partición.")
    
    # Imprimir la memoria usada y la memoria disponible después de asignar archivos
    print("\nEstado de la memoria:")
    for i in range(len(memoria_disponible)):
        print(f"Partición {i + 1}: {memoria_usada[i]}KB usados / {memoria_disponible[i]}KB disponibles")
    
    # Restablecer la memoria utilizada
    for i in range(len(memoria_usada)):
        memoria_disponible[i] += memoria_usada[i]

# Función para realizar la asignación de memoria con el algoritmo de mejor ajuste
def mejor_ajuste(archivos, memoria_disponible):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    
    for nombre_archivo, tamano_archivo in archivos:
        asignado = False
        mejor_particion = -1
        menor_diferencia = float('inf')
        
        for i in range(len(memoria_disponible)):
            if memoria_usada[i] == 0 and memoria_disponible[i] >= tamano_archivo:
                diferencia = memoria_disponible[i] - tamano_archivo
                if diferencia < menor_diferencia:
                    mejor_particion = i
                    menor_diferencia = diferencia
        
        if mejor_particion != -1:
            memoria_disponible[mejor_particion] -= tamano_archivo
            memoria_usada[mejor_particion] += tamano_archivo
            print(f"El archivo '{nombre_archivo}' de {tamano_archivo}KB se asignó a la partición {mejor_particion + 1} (Mejor ajuste).")
            asignado = True
        
        if not asignado:
            print(f"No se pudo asignar el archivo '{nombre_archivo}' de {tamano_archivo}KB a ninguna partición.")
    
    # Imprimir la memoria usada y la memoria disponible después de asignar archivos
    print("\nEstado de la memoria:")
    for i in range(len(memoria_disponible)):
        print(f"Partición {i + 1}: {memoria_usada[i]}KB usados / {memoria_disponible[i]}KB disponibles")
    
    # Restablecer la memoria utilizada
    for i in range(len(memoria_usada)):
        memoria_disponible[i] += memoria_usada[i]

# Función para realizar la asignación de memoria con el algoritmo de peor ajuste
def peor_ajuste(archivos, memoria_disponible):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    
    for nombre_archivo, tamano_archivo in archivos:
        asignado = False
        peor_particion = -1
        mayor_diferencia = -1
        
        for i in range(len(memoria_disponible)):
            if memoria_usada[i] == 0 and memoria_disponible[i] >= tamano_archivo:
                diferencia = memoria_disponible[i] - tamano_archivo
                if diferencia > mayor_diferencia:
                    peor_particion = i
                    mayor_diferencia = diferencia
        
        if peor_particion != -1:
            memoria_disponible[peor_particion] -= tamano_archivo
            memoria_usada[peor_particion] += tamano_archivo
            print(f"El archivo '{nombre_archivo}' de {tamano_archivo}KB se asignó a la partición {peor_particion + 1} (Peor ajuste).")
            asignado = True
        
        if not asignado:
            print(f"No se pudo asignar el archivo '{nombre_archivo}' de {tamano_archivo}KB a ninguna partición.")
    
    # Imprimir la memoria usada y la memoria disponible después de asignar archivos
    print("\nEstado de la memoria:")
    for i in range(len(memoria_disponible)):
        print(f"Partición {i + 1}: {memoria_usada[i]}KB usados / {memoria_disponible[i]}KB disponibles")
    
    # Restablecer la memoria utilizada
    for i in range(len(memoria_usada)):
        memoria_disponible[i] += memoria_usada[i]

# Función para realizar la asignación de memoria con el algoritmo de siguiente ajuste
def siguiente_ajuste(archivos, memoria_disponible):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    indice_siguiente = 0  # Índice de la próxima partición a considerar en el siguiente ajuste
    
    for nombre_archivo, tamano_archivo in archivos:
        asignado = False
        particiones_restantes = list(range(len(memoria_disponible)))  # Lista de particiones disponibles
        
        while len(particiones_restantes) > 0:
            i = indice_siguiente % len(particiones_restantes)
            particion_actual = particiones_restantes[i]
            
            if memoria_disponible[particion_actual] >= tamano_archivo:
                memoria_disponible[particion_actual] -= tamano_archivo
                memoria_usada[particion_actual] += tamano_archivo
                print(f"El archivo '{nombre_archivo}' de {tamano_archivo}KB se asignó al Siguiente ajuste en la partición {particion_actual + 1}.")
                asignado = True
                indice_siguiente = (particion_actual + 1) % len(memoria_disponible)  # Avanzar al siguiente espacio
                break
            
            particiones_restantes.pop(i)  # Eliminar la partición actual de las disponibles
        
        if not asignado:
            print(f"No se pudo asignar el archivo '{nombre_archivo}' de {tamano_archivo}KB a ninguna partición.")
    
    # Imprimir la memoria usada y la memoria disponible después de asignar archivos
    print("\nEstado de la memoria:")
    for i in range(len(memoria_disponible)):
        print(f"Partición {i + 1}: {memoria_usada[i]}KB usados / {memoria_disponible[i]}KB disponibles")
    
    # Restablecer la memoria utilizada
    for i in range(len(memoria_usada)):
        memoria_disponible[i] += memoria_usada[i]

# Función principal del programa
def main():
    archivos = []
    memoria_disponible = []

    # Leer archivos y memoria desde los archivos correspondientes
    archivos = leer_archivos()
    memoria_disponible = leer_memoria()

    if archivos and memoria_disponible:
        while True:
            print("\nMenú de opciones:")
            print("1. Asignar memoria (Primer ajuste)")
            print("2. Asignar memoria (Mejor ajuste)")
            print("3. Asignar memoria (Peor ajuste)")
            print("4. Asignar memoria (Siguiente ajuste)")
            print("5. Agregar memoria")
            print("6. Agregar proceso")
            print("7. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                primer_ajuste(archivos, memoria_disponible)
            elif opcion == "2":
                mejor_ajuste(archivos, memoria_disponible)
            elif opcion == "3":
                peor_ajuste(archivos, memoria_disponible)
            elif opcion == "4":
                siguiente_ajuste(archivos, memoria_disponible)
            elif opcion == "5":
                agregar_memoria(memoria_disponible)
            elif opcion == "6":
                agregar_proceso(archivos)
            elif opcion == "7":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
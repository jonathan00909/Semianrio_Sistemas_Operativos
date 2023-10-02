import os

# Definir la ruta al archivo que contiene la lista de archivos y tamaños
ruta_archivo = "C:\\Users\\jonat\\OneDrive\\Escritorio\\Practica\\archivos.txt"

# Definir las particiones de memoria disponibles
memoria_disponible = [1000, 400, 1800, 700, 900, 1200, 1500]

# Crear una función para asignar archivos a particiones de memoria usando el Primer ajuste
def primer_ajuste(archivos):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    
    for nombre_archivo, tamano_archivo in archivos.items():
        asignado = False
        
        for i in range(len(memoria_disponible)):
            if memoria_usada[i] == 0 and memoria_disponible[i] >= tamano_archivo:
                memoria_disponible[i] -= tamano_archivo
                memoria_usada[i] += tamano_archivo  # Actualizar la memoria usada en esta partición
                print(f"El archivo '{nombre_archivo}' de {tamano_archivo}KB se asignó a la partición {i + 1}.")
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

# Crear una función para asignar archivos a particiones de memoria usando el Mejor ajuste
def mejor_ajuste(archivos):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    
    for nombre_archivo, tamano_archivo in archivos.items():
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
            print(f"El archivo '{nombre_archivo}' de {tamano_archivo}KB se asignó al Mejor ajuste en la partición {mejor_particion + 1}.")
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

# Crear una función para asignar archivos a particiones de memoria usando el Peor ajuste
def peor_ajuste(archivos):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    
    for nombre_archivo, tamano_archivo in archivos.items():
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
            print(f"El archivo '{nombre_archivo}' de {tamano_archivo}KB se asignó al Peor ajuste en la partición {peor_particion + 1}.")
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

# Crear una función para asignar archivos a particiones de memoria usando el Siguiente ajuste
def siguiente_ajuste(archivos):
    os.system('cls' if os.name == 'nt' else 'clear')
    memoria_usada = [0] * len(memoria_disponible)  # Lista para rastrear la memoria usada en cada partición
    indice_siguiente = 0  # Índice de la próxima partición a considerar en el siguiente ajuste
    
    for nombre_archivo, tamano_archivo in archivos.items():
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

# Crear una función para mostrar el menú y manejar la selección del usuario
def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la pantalla
        
        print("\nMenú:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        print("3. Peor ajuste")
        print("4. Siguiente ajuste")
        print("0. Terminar")
        seleccion = input("Seleccione una opción: ")

        if seleccion == "1":
            try:
                # Leer el archivo de texto que contiene la lista de archivos y tamaños
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    lineas = archivo.readlines()

                archivos = {}

                # Procesar cada línea del archivo
                for linea in lineas:
                    # Dividir la línea en nombre y tamaño usando ','
                    nombre_archivo, tamano_archivo_texto = linea.strip().split(',')

                    # Eliminar espacios en blanco alrededor del nombre del archivo
                    nombre_archivo = nombre_archivo.strip()

                    # Eliminar el sufijo "kb" y luego convertir a un número entero
                    tamano_archivo = int(tamano_archivo_texto.strip()[:-2])

                    archivos[nombre_archivo] = tamano_archivo
                
                primer_ajuste(archivos)
                input("\nPresione Enter para continuar...")
            except FileNotFoundError:
                print("El archivo de texto no se encontró en la ruta especificada.")
                input("Presione Enter para continuar...")
        elif seleccion == "2":
            try:
                # Leer el archivo de texto que contiene la lista de archivos y tamaños
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    lineas = archivo.readlines()

                archivos = {}

                # Procesar cada línea del archivo
                for linea in lineas:
                    # Dividir la línea en nombre y tamaño usando ','
                    nombre_archivo, tamano_archivo_texto = linea.strip().split(',')

                    # Eliminar espacios en blanco alrededor del nombre del archivo
                    nombre_archivo = nombre_archivo.strip()

                    # Eliminar el sufijo "kb" y luego convertir a un número entero
                    tamano_archivo = int(tamano_archivo_texto.strip()[:-2])

                    archivos[nombre_archivo] = tamano_archivo
                
                mejor_ajuste(archivos)
                input("\nPresione Enter para continuar...")
            except FileNotFoundError:
                print("El archivo de texto no se encontró en la ruta especificada.")
                input("Presione Enter para continuar...")
        elif seleccion == "3":
            try:
                # Leer el archivo de texto que contiene la lista de archivos y tamaños
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    lineas = archivo.readlines()

                archivos = {}

                # Procesar cada línea del archivo
                for linea in lineas:
                    # Dividir la línea en nombre y tamaño usando ','
                    nombre_archivo, tamano_archivo_texto = linea.strip().split(',')

                    # Eliminar espacios en blanco alrededor del nombre del archivo
                    nombre_archivo = nombre_archivo.strip()

                    # Eliminar el sufijo "kb" y luego convertir a un número entero
                    tamano_archivo = int(tamano_archivo_texto.strip()[:-2])

                    archivos[nombre_archivo] = tamano_archivo
                
                peor_ajuste(archivos)
                input("\nPresione Enter para continuar...")
            except FileNotFoundError:
                print("El archivo de texto no se encontró en la ruta especificada.")
                input("Presione Enter para continuar...")
        elif seleccion == "4":
            try:
                # Leer el archivo de texto que contiene la lista de archivos y tamaños
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    lineas = archivo.readlines()

                archivos = {}

                # Procesar cada línea del archivo
                for linea in lineas:
                    # Dividir la línea en nombre y tamaño usando ','
                    nombre_archivo, tamano_archivo_texto = linea.strip().split(',')

                    # Eliminar espacios en blanco alrededor del nombre del archivo
                    nombre_archivo = nombre_archivo.strip()

                    # Eliminar el sufijo "kb" y luego convertir a un número entero
                    tamano_archivo = int(tamano_archivo_texto.strip()[:-2])

                    archivos[nombre_archivo] = tamano_archivo
                
                siguiente_ajuste(archivos)
                input("\nPresione Enter para continuar...")
            except FileNotFoundError:
                print("El archivo de texto no se encontró en la ruta especificada.")
                input("Presione Enter para continuar...")
        elif seleccion == "0":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

# Llamar a la función del menú
menu()

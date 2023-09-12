import os
import shutil

# Obtiene la ruta del directorio actual donde se encuentra el archivo .py
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Ruta de la carpeta origen
carpeta_origen = os.path.join(directorio_actual, "carpeta_original")

# Ruta de la carpeta de destino (donde se copiarán los archivos)
carpeta_destino = os.path.join(directorio_actual, "carpeta_copia")

# Función para copiar la carpeta origen y sus contenidos a la carpeta destino
def copiar_carpeta_origen_a_destino(origen, destino):
    try:
        shutil.copytree(origen, destino) #copia la carpeta completamente
        print(f"Carpeta '{origen}' copiada exitosamente a '{destino}'.")
    except FileExistsError:
        print(f"La carpeta destino '{destino}' ya existe.")

# Llamar a la función para copiar la carpeta
copiar_carpeta_origen_a_destino(carpeta_origen, carpeta_destino)

# Función para renombrar carpetas y archivos TXT en la carpeta destino
def renombrar_carpetas_y_archivos_en_destino(ruta):
    for root, dirs, files in os.walk(ruta):
        for dir_name in dirs:
            ruta_original = os.path.join(root, dir_name)
            
            # Reemplazar números por letras y viceversa en el nombre
            nuevo_nombre = "".join(str(ord(char) - 96) if char.isalpha() else chr(int(char) + 96) if char.isdigit() else char for char in dir_name.lower())

            # Ruta completa de la carpeta original y la nueva carpeta
            ruta_nueva = os.path.join(root, nuevo_nombre)

            # Renombrar la carpeta
            os.rename(ruta_original, ruta_nueva)
            print(f"Renombrada carpeta '{ruta_original}' a '{ruta_nueva}'")

        for file_name in files:
            if file_name.endswith(".txt"):
                ruta_original = os.path.join(root, file_name)
                nombre_sin_extension, extension = os.path.splitext(file_name)
                
                # Reemplazar números por letras y viceversa en el nombre del archivo
                nuevo_nombre = "".join(str(ord(char) - 96) if char.isalpha() else chr(int(char) + 96) if char.isdigit() else char for char in nombre_sin_extension.lower()) + extension

                # Ruta completa del archivo original y el nuevo archivo
                ruta_nuevo = os.path.join(root, nuevo_nombre)

                # Renombrar el archivo
                os.rename(ruta_original, ruta_nuevo)
                print(f"Renombrado archivo '{ruta_original}' a '{ruta_nuevo}'")

# Llamar a la función para renombrar carpetas y archivos en la carpeta destino
renombrar_carpetas_y_archivos_en_destino(carpeta_destino)

import os

# Función para convertir una dirección IPv6 en formato hexadecimal a decimal
def ipv6_hex_a_dec(hex_ip): #ipv6_hex_a_decimal toma como argumento hex_ip
    hex_secciones = hex_ip.split(':')  # Dividir la dirección en secciones hexadecimales
    dec_secciones = []
    
    for hex_seccion in hex_secciones:
        if '/' in hex_seccion:  # Si hay una máscara de subred
            parte_ip, mascara_subred = hex_seccion.split('/')  # Dividir dirección y máscara
            dec_parte_ip = str(int(parte_ip, 16))  # Convertir sección a decimal
            dec_mascara_subred = str(int(mascara_subred, 16))  # Convertir máscara a decimal
            dec_seccion = f"{dec_parte_ip}/{dec_mascara_subred}"  # Combinar dirección y máscara
        else:
            dec_seccion = str(int(hex_seccion, 16))  # Convertir sección a decimal
        dec_secciones.append(dec_seccion)  # Agregar sección a la lista
    
    return ':'.join(dec_secciones)  # Combinar secciones en dirección IPv6 decimal

# Función para convertir una dirección IPv4 decimal a hexadecimal en mayúsculas
def ipv4_dec_a_hex(ipv4):
    octetos_decimales = ipv4.split('.')  # Dividir la dirección en octetos decimales
    octetos_hexadecimales = [format(int(octeto), 'X') for octeto in octetos_decimales]  # Convertir a hexadecimal en mayúsculas
    return ':'.join(octetos_hexadecimales)  # Combinar octetos en dirección IPv4 hexadecimal

# Obtener la ruta del directorio donde se encuentra el archivo .py
directorio_actual = os.path.dirname(os.path.abspath(__file__))

# Construir rutas de entrada y salida en el mismo directorio que el archivo .py
ruta_archivo_entrada = os.path.join(directorio_actual, 'prueba2.txt')
ruta_archivo_salida = os.path.join(directorio_actual, 'salida.txt')

# Abrir archivos de entrada y salida
with open(ruta_archivo_entrada, 'r') as archivo_entrada, open(ruta_archivo_salida, 'w') as archivo_salida:
    for linea in archivo_entrada:
        campos = linea.strip().split(',')  # Dividir la línea en campos
        
        if len(campos) == 6:  # Si hay 6 campos en la línea
            hex_ip = campos[0]
            dec_ip = ipv6_hex_a_dec(hex_ip)  # Convertir dirección IPv6 a decimal
            nombre = campos[2]  # Tomar el segundo campo (nombre)
            ipv4 = campos[5]  # Tomar el sexto campo (IPv4)
            hex_ipv4 = ipv4_dec_a_hex(ipv4)  # Convertir IPv4 a hexadecimal
            
            # Construir la línea de salida en el formato "nombre:IPv6/IPv4"
            linea_salida = f"{nombre}:{dec_ip}:{hex_ipv4}\n"
            archivo_salida.write(linea_salida)  # Escribir la línea de salida en el archivo

            # Imprimir mensaje de transformación en la consola
            mensaje = f"La entrada: {linea.strip()} ha sido transformada a {linea_salida.strip()}"
            print(mensaje)
print("Procesamiento por lotes completado.")

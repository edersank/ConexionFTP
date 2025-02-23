from ftplib import FTP
import os
        
#Datos servidor
host = "ftp.byethost7.com"
user = "b7_38369860"
password = "Temporal2025"
import time


try:
    ftp = FTP(host, user, password)
    print("Conexion establecida...")
    
    #Muesta la carpeta acutal /Raiz
    ftp.cwd("htdocs")
    print("..")
    print(ftp.pwd())
    
    #Ver  los archivos de la carpeta acutal
    print()
    ftp.dir()
    
    nombre_archivo = "archivo_desde_python.txt"
    abrir_archivo = open(nombre_archivo, 'wb')
    #crea el archivo y hace una copia de lo que contiene el archivo
    ftp.retrbinary("RETR " + nombre_archivo, abrir_archivo.write)
    
except Exception as e:
    print("Error en la conexion: " + str(e))
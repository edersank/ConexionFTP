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
    print("..")
    print(ftp.pwd())
    
    #Ver  los archivos de la carpeta acutal
    print()
    ftp.dir()
    
    #Acceder a directorio .cwd()
    print()
    print("..")
    ftp.cwd("htdocs")
    print(ftp.pwd())
    ftp.dir()
    
    
    #Crear carpeta
    # ftp.mkd("dir_desde_python")
    #Crear achivo
    #Crea el archivo local
    # with open("archivo_desde_python.txt", "w") as archivo:
    #     archivo.write("Archivo creado desde python\nCon conexion a ftp")
    #     archivo.close()
    #     archivo = open("archivo_desde_python.txt", "rb")
    # #.storbinary("STOR nombre del archivo", ubicacion del archivo)
    #     ftp.storbinary("STOR archivo_desde_python.txt", archivo)
    #     time.sleep(2)
    #     archivo.close()
        
    # os.remove("archivo_desde_python.txt")
    # ftp.dir()
except Exception as e:
    print("Error en la conexion: " + str(e))
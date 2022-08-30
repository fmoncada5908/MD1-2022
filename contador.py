from io import open
import sys

fichero = open("contador.txt","a+")
fichero.seek(0)
contenido = fichero.redline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)
    
fichero.close()

#vamos a transformar el texto a numero

try:
    contador = int(contenido)
    #En relación a lo que el usuario necesite
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
            
    print(contador)
    
    #Volvemos a escribir los cambios en el fichero.
    fichero = open("contador.txt", "w")
    fichero.write(str(contador))
    fichero.close()

except:
    print("Error: Fichero Corrupto")    
        
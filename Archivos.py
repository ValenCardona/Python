print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tEjercicios Archivos ")
from io import open

print ("\n\t\t1. Crear un archivo que inserte diez líneas en un archivo de nombre archivo2.txt ")

cantidad = int(input("\n\tDigitela la cantidad de persona que desea ingresar"))
archivoTexto = open ("archivo2.txt","w")
for x in range (cantidad):
    nombre = input("\tDigite El Nombre: ")
    cedula = input("\tDigite la Cedula: ")
    numeroCelular = input("\tDigite el numero del celular: ")
    frase = ("\n"+ str(x) + "."+"\tNombre: " +nombre+"\tCedula: "+cedula+"\tNumero celular: "+numeroCelular)
    archivoTexto.write(frase)
archivoTexto.close()

print ("\n\t\t2. Crear un archivo de nombre archivo3.txt, que solicite a un usuario una tabla de multiplicar e imprima dicha tabla hasta el 20 ")

archivoTexto = open ("archivo3.txt","w")
tabla =  int(input("\tDigite la tabla de multiplicar: "))
for x in range (0, 21):
    archivoTexto.write("\n"+str(tabla) + "x" + str(x) + " = " + str(tabla * x))  
archivoTexto.close()

print ("\n\t\t3. Mostrar en un archivo archivo4.txt, los resultados del programa de operaciones matemáticas ")

from Operaciones_basicas import *

print ("\n\t\t4. Liquidar dos empleados de la nómina y guardar los resultados generados en un archivo" )

from Nomina import *

print ("\n\t\t 5.Escribir una función que pida dos números `n` y `m` entre 1 y 10, lea el fichero `tabla-n.txt` con la tabla de multiplicar de ese número, y muestre por pantalla la línea `m` del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.")

n = int(input('\tIntroduce un número entero entre 1 y 10: '))
fileName = 'tabla-' + str(n) + '.txt'
f = open("archivo6.txt", 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()


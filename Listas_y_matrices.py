print ("\n\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tListas y matrices")

print ("\t\t\tMetodos de listas")

lista = []
tamaño = int(input("\tDigite el tamaño de la lista: "))

for x in range(tamaño):
    print("\tDigite el numero entero que quiere para la posición: [",x,"]")
    valor = float(input("\t"))
    lista.append(valor)

print ("\t", lista)
suma = sum(lista)
maximo = max(lista)
minimo = min(lista)
tam = len(lista)
promedio = suma/tam
lista.sort()

print("\t La suma de toda la lista es: ", round(suma))
print("\t El numero maximo de toda la lista es: ", maximo)
print("\t El numero minimo de toda la lista es: ", minimo)
print("\t El tamaño de la lista es: ", tam)
print("\t El promedio de los datos de la lista es: ", round(promedio))
print("\t El orden de la lista es: ", lista)

lista1 = ['a', 'b', 'c']
print("\t La lista inicial es: ", lista1)
tamaño = int(input("\tDigite el tamaño de la lista: "))

for x in range(tamaño):
    letra = input("\tIngrese una letra diferente : ")
    lista1.extend(letra)

print("\t", lista1)
tamaño = len(lista1)
lista1.sort()
print("\t El tamaño de la lista es: ", tamaño)
print("\t La lista ordenada: ", lista1)

print ("\t\t\tEjercicios Matrices")

print ("\t1. Escribir un algoritmo que permita sumar el número de elementos positivos y el de negativos de una tabla T de n filas y m columnas. Sumar por filas y por columnas los elementos de la matriz. Contar el número de elementos positivos y negativos")
matriz = []
filas = int(input("\tDigite cantidad de filas: "))
columnas = int(input("\tDigite cantidad de columnas: "))

for x in range(filas):
    matriz.append([0]*columnas)
    
for a in range(filas):
    for b in range(columnas):
        print ("\tDigite el numero para almacenar en la posición [",a,"]", "[",b,"]" )
        matriz[a][b] = float(input("\t"))
      
print ("\t", matriz)
suma = 0
acumPositivos = 0
acumNegativos = 0

for a in range(filas):
    for b in range(columnas):
        if (matriz [a][b]>=0):
            acumPositivos = acumPositivos + matriz [a][b]
        else:     
            acumNegativos = acumNegativos + matriz [a][b]
        suma = suma + matriz [a][b]
    print ("\tLa suma de la fila [", a, "]: ",suma)
    suma=0

for b in range(columnas):
    for a in range(filas):
        suma = suma + matriz [a][b]
    print ("\tLa suma de la columna [", b, "]: ",suma)
    suma=0

print ("\tAcumulador de Positivos",acumPositivos)
print ("\tAcumulador de Negativos",acumNegativos)

print ("\t 2. Este programa saca el promedio de nota de cada estudiante y de cada materia")
matriz = []
filas = int(input("\tDigite cantidad de materias: "))
columnas = int(input("\tDigite cantidad de estudiantes: "))

for x in range(filas):
    matriz.append([0]*columnas)
for a in range(filas):
    for b in range(columnas):
        print ("\tDigite la nota de cada estudiante [",a," ]", "[",b,"], recuede que la calificación va de (1.0 a 5.0): " )  
        matriz [a][b]= float(input("\t"))
        if matriz[a][b] < 1.0 or matriz[a][b] >5.0:
            print("\tNota no valida, ingrese nuevamente la calificación")
            print ("\tDigite la nota de cada estudiante [",a," ]", "[",b,"], recuede que la calificación va de (1.0 a 5.0): " )  
            matriz [a][b]= float(input("\t"))

print (matriz)

suma = 0
acumulador_positivos = 0
acumulador_negativos = 0

for a in range(filas):
    for b in range(columnas):
        suma = suma + matriz [a][b]
        promedio=suma/columnas
    print ("\tEl promedio de la materia [", a, "]es: ",promedio)
    suma=0
for b in range(columnas):
    for a in range(filas):
        suma = suma + matriz [a][b]
        promedio=suma/filas
    print ("\tEl promedio del estudiante [", b, "]es: ",promedio)
    suma=0

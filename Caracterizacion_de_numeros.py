print("\n\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tPrograma que caracteriza los numeros en positivos, negativos o ceros mediante ciclos")

print("\t\t\t Ciclo while")

contPositivos = 0
acumPositivos = 0
contNegativos = 0
acumNegativos = 0
contNeutros = 0
acumNeutros = 0
contProcesos = 1   
listaNumero = int(input("\tDigite la cantidad de numeros a categorizar:   "))

while contProcesos <= listaNumero:

    numero = int(input("\tDigite un numero, positivo, negativo o neutro(0): "))
    if(numero > 0):
        contPositivos = contPositivos + 1
        acumPositivos = acumPositivos + numero    
    elif(numero < 0):
        contNegativos = contNegativos + 1
        acumNegativos = acumNegativos + numero
    else:
        contNeutros = contNeutros + 1
        acumNeutros = acumNeutros + numero

    contProcesos = contProcesos + 1

print ("\n\t Resultados del Procesos de Caracterizacion de Numeros")
print ("\n\t Cantidad de Numeros Ingresados es: ", listaNumero)
print ("\n\t Cantidad de Numeros Positivos son: ", contPositivos)
print ("\n\t Suma de Numeros Positivos es: ", acumPositivos)
print ("\n\t Cantidad de Numeros Negativos son: ", contNegativos)
print ("\n\t Suma de Numeros Negativos es: ", acumNegativos)
print ("\n\t Cantidad de Numeros Neutros son: ", contNeutros)
print ("\n\t Suma de Numeros Neutros es: ", acumNeutros)

print ("\t\t Ciclo for")

contPositivos = 0
acumPositivos = 0
contNegativos = 0
acumNegativos = 0
contNeutros = 0
acumNeutros = 0
contProcesos = 0
listaNumero = int(input("\tDigite la cantidad de numeros a categorizar:   "))

for contProcesos in range (0,listaNumero):

    numero = int(input("\tDigite un numero, positivo, negativo o neutro(0): "))
    if(numero > 0):
        contPositivos = contPositivos + 1
        acumPositivos = acumPositivos + numero    
    elif(numero < 0):
        contNegativos = contNegativos + 1
        acumNegativos = acumNegativos + numero
    else:
        contNeutros = contNeutros + 1
        acumNeutros = acumNeutros + numero

print ("\n\t Resultados del Procesos de Caracterizacion de Numeros")
print ("\n\t Cantidad de Numeros Ingresados es: ", listaNumero)
print ("\n\t Cantidad de Numeros Positivos son: ", contPositivos)
print ("\n\t Suma de Numeros Positivos es: ", acumPositivos)
print ("\n\t Cantidad de Numeros Negativos son: ", contNegativos)
print ("\n\t Suma de Numeros Negativos es: ", acumNegativos)
print ("\n\t Cantidad de Numeros Neutros son: ", contNeutros)
print ("\n\t Suma de Numeros Neutros es: ", acumNeutros)

    

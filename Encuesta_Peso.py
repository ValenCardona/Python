print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque")
print ("\n\tUna persona desea realizar un muestreo con n personas para determinar el promedio de peso de los niños, jóvenes, adultos y viejos que existen en su zona habitacional y cuantos son de cada uno de las categorías. Se determinan las categorías con base en la siguiente tabla")
print ("\tCATEGORIAS |	EDAD")
print ("\t------")
print ("\tNiños      |	0 – 13")
print ("\tJóvenes    |	14 – 30")
print ("\tAdultos    |	31 – 60")
print ("\tViejos     | 	61 en adelante")


print("\tBienvenido a la estadistica del peso de la población")
nuevoRegistro = "si"
promedio = 0
niños = 0
jovenes = 0
adultos = 0
viejos = 0
contNiño = 0
contJoven = 0
contAdulto = 0
contViejo = 0
suma = 0

while nuevoRegistro == "si" :

  nombre = input("\tDigite el nombre de la persona: ")
  edad = int(input("\tDigite la edad de la persona: "))
  
  if edad < 0:
    print("\tLa edad ingresada no es correcta")
    edad = int(input("\tDigite la edad de la persona: "))
  peso = int(input("\tDigite el peso de la persona: "))
  
  if (edad >= 0) and (edad <= 13):
    niños = niños + peso
    contNiño = contNiño + 1
  elif (edad >= 14) and (edad <= 30):
    jovenes = jovenes + peso
    contJoven = contJoven + 1
  elif (edad >= 31) and (edad <=60 ):
    adultos = adultos + peso
    contAdulto = contAdulto + 1
  elif (edad >= 61):
    viejos = viejos + peso
    contViejo = contViejo + 1  
 
  nuevoRegistro = input("\tDesea ingresar a otra persona si/ no: ")

suma = (niños + jovenes + adultos + viejos)
suma1 = contNiño + contJoven + contAdulto + contViejo

if contNiño == 0:
  promedioNiños = 0
else:
  promedioNiños = niños/contNiño
if contJoven == 0:
  promedioJovenes = 0
else:
  promedioJovenes = jovenes/contJoven
if contAdulto == 0:
  promedioAdultos = 0
else:
  promedioAdultos = adultos/contAdulto 
if contViejo == 0:
  promedioViejos = 0
else:
  promedioViejos = viejos/contViejo
promedio = suma/suma1 

print("\tLa cantidad de niños encuestados es de: ", contNiño)
print("\tEl promedio de los pesos de los niños es ", promedioNiños, "Kg")
print("\tLa cantidad de jovenes encuestados es de: ", contJoven)
print("\tEl promedio de los pesos de los jovenes es ", promedioJovenes, "Kg")
print("\tLa cantidad de adultos encuestados es de: ", contAdulto)
print("\tEl promedio de los pesos de los adultos es ", promedioAdultos, "Kg")
print("\tLa cantidad de adultos mayores de 61 años encuestados es de: ", contViejo)
print("\tEl promedio de los pesos de los adultos mayores de 61 años es ", promedioViejos, "Kg")
print("\tEl promedio de los pesos de todas las personas encuestadas es: ", promedio)

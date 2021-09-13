print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tCalcular y visualizar la longitud de la circunferencia y el área de un círculo de radio dado.")

from math import pi

radio = int(input("\tDigite el radio de la circunferencia en metros(m): "))

longitud = 2 * pi * radio
area = pi * radio**2

print("\tLa longitud de una circunferencia es ->", 2, "*", pi, "*", radio, "=", longitud, "m")
print("\tEl area de una circunferencia es: ", pi, "*", radio,"^2", "=", area,"m^2")

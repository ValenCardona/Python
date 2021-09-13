print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tEscribir un algoritmo que calcule la superficie de un triángulo en función de la base y la altura (S = ½ × Base × Altura)")

base = int(input("\tDigite el valor de la base en metro(m): "))
altura = int(input("\tDigite el valor de la altura en metros (m): "))

s = (base*altura)//2

print("\tLa superficie de un triangulo es: (", base, "*", altura, ")/2", "=", s,"m^2")

print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tRealizar las operaciones matemáticas basicas: suma, resta, multiplicación, división, residuo y potencia.")

numero1 = int(input("\tDigite el primer número: "))
numero2 = int(input("\tDigite el segundo número: "))
numero3 = 5

suma = numero1 + numero2 + numero3
resta = numero1 - numero2 - numero3
producto = numero1 * numero2 * numero3
division = numero1 // numero2 // numero3
residuo = numero1 % numero2 % numero3
potencia = (numero1 ** numero2) ** numero3

print("\tResultado suma ->", numero1, "+", numero2, "+", numero3, "=", suma)
print("\tResultado resta -> ", numero1, "-", numero2, "-", numero3, "=", resta)
print("\tResultado multiplicación -> ", numero1, "*", numero2, "*", numero3, "=", producto)
print("\tResultado divisiones -> ", numero1, "/", numero2, "/", numero3, "=", division)
print("\tResultado residuo -> ", numero1, "%", numero2, "%", numero3, "=", residuo)
print("\tResultado potencia -> ", numero1, "^", numero2, "^", numero3, "=", round(potencia))

archivoTexto = open ("archivo4.txt", "a")
archivoTexto.write("\n\t Operaciones matemáticas basicas")
archivoTexto.write("\n\t Suma-> " + str(numero1) + "+" + str(numero2) + "+" + str(numero3) + "=" + str(suma))
archivoTexto.write("\n\t Resta-> " + str(numero1) + "-" + str(numero2) + "-" + str(numero3) + "=" + str(suma))
archivoTexto.write("\n\t Multiplicación-> " + str(numero1) + "*" + str(numero2) + "*" + str(numero3) + "=" + str(suma))
archivoTexto.write("\n\t División-> " + str(numero1) + "/" + str(numero2) + "/" + str(numero3) + "=" + str(suma))
archivoTexto.write("\n\t Residuo-> " + str(numero1) + "%" + str(numero2) + "%" + str(numero3) + "=" + str(suma))
archivoTexto.write("\n\t Potnecia-> " + str(numero1) + "^" + str(numero2) + "^" + str(numero3) + "=" + str(suma))

print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tEscribir un algoritmo que encuentre el salario semanal de un trabajador, dada la tarifa horaria y el número de horas trabajadas diariamente.")


tarifa = int(input("\tDigite la tarifa horarioa del trabajdor: $"))
horasLunes = int(input("\tDigite la cantidad de horas trabajadas el lunes: "))
horasMartes = int(input("\tDigite la cantidad de horas trabajadas el martes: "))
horasMiercoles = int(input("\tDigite la cantidad de horas trabajadas el miercoles: "))
horasJueves = int(input("\tDigite la cantidad de horas trabajadas el jueves: "))
horasViernes = int(input("\tDigite la cantidad de horas trabajadas el viernes: "))
horasSabado = int(input("\tDigite la cantidad de horas trabajadas el sabado: "))
horasDomingo = int(input("\tDigite la cantidad de horas trabajadas el domingo: "))

horasTotal = horasLunes + horasMartes + horasMiercoles + horasJueves + horasViernes + horasSabado + horasDomingo
salarioSemanal = horasTotal * tarifa

print("\tEl salario semanal del trabajador es: ", salarioSemanal)

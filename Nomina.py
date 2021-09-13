print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tElabore una nómina de un empleado.")

reiniciar = "si"
pagoTotalNomina = 0
contLiquidacion = 0

while reiniciar == "si":

  contLiquidacion = contLiquidacion + 1  
  cedula = int(input("\tDigite la cedula del empleado: "))
  nombre = input("\tDigite el nombre del empleado: ")
  salario = int(input("\tDigite el salario del empleado: "))
  dias = int(input("\tDigite los días que trabajo el empleado: "))
  numeroHed = int(input("\tDigite el numero de horas extras diurnas que laboro el empleado: "))
  numeroHen = int(input("\tDigite el numero de horas extras nocturnas que laboro el empleado: "))
  numeroHef = int(input("\tDigite el numero de horas extras de días festivos que laboro el empleado: "))
  diasNoche = int(input("\tDigite el numero de dias nocturnos que laboro el empleado: "))
  prestamo = input("\tDigite si el empleado tiene algun prestamo: ")

  #Inicio Saldo devengado
  
  sueldo = salario / 30 * dias
  valorHed = salario/240 * 1.25 * numeroHed
  valorHen = salario/240 * 1.75 * numeroHen
  valorHef = salario/240 * 2 * numeroHef

  if salario <= 1817052:
    subsidio = 106454/30 * dias
  else:
    subsidio =0
  
  if diasNoche > 0:
    recargoNocturno = salario/30 * diasNoche * 1.35
  else:
    recargoNocturno = 0
  
  totalDevengado = sueldo + subsidio + valorHed + valorHen + valorHef + recargoNocturno

  #Inicio Deucido

  salud = (totalDevengado - subsidio) * 4/100
  pension = (totalDevengado - subsidio) * 4/100

  if (salario >= 3634104) and (salario < 14536416):
    fondo = salario * 1/100
  elif (salario >= 14536416) and (salario < 15444942):
    fondo = salario * 1.2/100
  elif (salario >= 15444942) and (salario < 16353468):
    fondo = salario * 1.4/100
  elif (salario >= 16353468) and (salario < 17261994):
    fondo = salario * 1.6/100
  elif (salario >= 17261994) and (salario < 18170520):
    fondo = salario * 1.8/100
  elif (salario >= 18170520):
    fondo = salario * 2/100
  else:
    fondo = 0

  if (prestamo == "si") or (prestamo == "Si"):
    valorPrestamo = int(input("\tDigite el valor de la cuota del prestamo: $"))
  else:
    valorPrestamo = 0
  
  totalDeducido = salud + pension + fondo + valorPrestamo
  valorNeto = totalDevengado - totalDeducido

  print("\tCedula del empleado: ", cedula)
  print("\tNombre del empleado: ", nombre)
  print("\tSalario base es: $",salario)
  print("\tLos días laborados son: ",dias)
  print("\tEl número de horas extras diurnas es:", numeroHed)
  print("\tEl número de horas extras nocturnas es:", numeroHen)
  print("\tEl número de horas extras en un día festivo es:", numeroHef)
  print("\tEl número de días laborados en la noche es:", diasNoche)
  print("\t-------------------------------------")
  print("\tSaldo devengado")
  print("\tSueldo: $",sueldo)
  print("\tAuxilio de transporte: $",subsidio)
  print("\tValor de las horas extras diurnas: $",valorHed)
  print("\tValor de las horas extras nocturas: $",valorHen)
  print("\tValor de las horas extras trabajadas en un día festivo: $", valorHef)
  print("\tValor del recargo nocturno: $",recargoNocturno)
  print("\tTotal devengado es: $",totalDevengado)
  print("\t----------------------------------")
  print("\tSaldo deducido")
  print("\tValor a pagar por salud: $",salud)
  print("\tValor a pagar por pensión: $",pension)
  print("\tValor a pagar por el fondo solidario: $",fondo)
  print("\tValor a pagar por prestamo: $",valorPrestamo)
  print("\tTotal deducido es: $",totalDeducido)
  print("\t---------------------------------")
  print("\tValor neto a pagar es: $", round(valorNeto))
  print("\t----------------------------------")
  
  pagoTotalNomina = round(pagoTotalNomina + valorNeto)
  reiniciar = input("\tDesea liquidar otro empleado (si/no): ")
  print("\t----------------------------------")
  print("\t----------------------------------")
  print("\tValor total de la nomina a pagar por los", contLiquidacion, " empleados es: $", pagoTotalNomina)
  print("\t----------------------------------")
  print("\t----------------------------------")

  archivoTexto = open ("archivo5.txt","a")
  archivoTexto.write("\n\t Liquidación de nomina de dos empleados")
  archivoTexto.write("\n\t Empleado No. " + str(contLiquidacion))
  archivoTexto.write("\n\t Nombre del empleado: " + nombre)
  archivoTexto.write("\n\t Cedula del empleado: " + str(cedula))
  archivoTexto.write("\n\t Salario del empleado: $" + str(salario))
  archivoTexto.write("\n\t Días laborados del empleado: " + str(dias))
  archivoTexto.write("\n\t El número de horas extras diurnas laboradas por el empleado son: " + str(numeroHed))
  archivoTexto.write("\n\t El número de horas extras nocturnas laboradas por el empleado son: " + str(numeroHen))
  archivoTexto.write("\n\t El número de horas extras en un dia festivo laboradas por el empleado son: " + str(numeroHef))
  archivoTexto.write("\n\t El número de días laborados en la noche por el empleado son: " + str(diasNoche))
  archivoTexto.write("\n\t--------------------------------")
  archivoTexto.write("\n\t Saldo devengado")
  archivoTexto.write("\n\t Sueldo del empleado: $" + str(sueldo))
  archivoTexto.write("\n\t Auxilio de transporte del empleado: $" + str(subsidio))
  archivoTexto.write("\n\t Valor de las horas extras diurnas del empleado: $" + str(valorHed))
  archivoTexto.write("\n\t Valor de las horas extras nocturnas del empleado: $" + str(valorHen))
  archivoTexto.write("\n\t Valor de las horas extras en un dia festivo del empleado: $" + str(valorHef))
  archivoTexto.write("\n\t Valor del recargo nocturno del empleado: $" + str(recargoNocturno))
  archivoTexto.write("\n\t Total devengado del empleado es: $" + str(totalDevengado))
  archivoTexto.write("\n\t--------------------------------")
  archivoTexto.write("\n\t Saldo deducido")
  archivoTexto.write("\n\t Valor a pagar por la salud del empleado es: $" + str(salud))
  archivoTexto.write("\n\t Valor a pagar por la pension del empleado es: $" + str(pension))
  archivoTexto.write("\n\t Valor a pagar por el fondo solidario del empleado es: $" + str(fondo))
  archivoTexto.write("\n\t Valor a pagar por el prestamo del empleado es: $" + str(valorPrestamo))
  archivoTexto.write("\n\t Total deducido del empleado es: $" + str(totalDeducido))
  archivoTexto.write("\n\t--------------------------------")
  archivoTexto.write("\n\t Valor neto a pagarle al empleado es: $" + str(round(valorNeto)))
  archivoTexto.write("\n\t--------------------------------")
  archivoTexto.write("\n\t El valor total de la nomina a pagar de los " + str(contLiquidacion) + "empleados es: $" + str(pagoTotalNomina))
  archivoTexto.write("\n\t--------------------------------")
  archivoTexto.close()
  


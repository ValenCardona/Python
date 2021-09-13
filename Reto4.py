print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tReto 4")
"""
El departamento de Talento Humano de la Universidad El Bosque, a raíz de la participación en un proyecto muy especial, requiere poder procesar la nómina de docentes contratados por horas. Para tal efecto ha establecido los siguientes lineamientos:
• La nómina será procesada semanalmente, digitando por cada docente las horas trabajadas en la semana y el valor establecido por hora.
• A todos los docentes que trabajen más de 40 horas en la semana, se les reconocerán como horas extras y se pagarán a un valor de 1,5 de la hora normal.
• Al salario bruto obtenido en el punto anterior se le calculará el 9% para los parafiscales.
• Para cada docente se le calcularán provisiones para prima de servicio 8.33%, cesantías 8.33%, intereses de cesantía 1.0% y vacaciones 4.17%.
• A cada uno se le descontará el aporte de 4% para salud y el 4% para pensión.
El director de Talento Humano le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python que le permita:

• Leer desde el teclado los datos de nombre, horas trabajadas y valor hora, por cada docente del proyecto.
• Mostrar en consola el sueldo bruto.
• Mostrar en consola los descuentos por parafiscales, salud y pensión.
• Mostrar en consola el sueldo neto a pagar.
• Mostrar en consola las provisiones hechas para prima, cesantías, intereses de cesantía y vacaciones.
• Los cálculos de sueldo bruto, descuentos, sueldo neto y provisiones, deberán ser realizados a través de funciones o procedimientos y serán llamados en el programa principal.
"""
personaNueva = "si"

while personaNueva == "si":
  def informacion():
    
    global horas, valorHora
    nombre = input("\tDigite el nombre del docente: ")
    horas = float(input("\tDigite la cantidad de horas semanales trabajadas por el docente: "))
    valorHora = int(input("\tDigite el valor de cada hora laborada: $"))
    return horas, valorHora

  def salario():

    if horas > 0 or horas <= 40:
      sueldoBruto = horas * valorHora
    if horas > 40:
      salarioSinHorasExtras = 40 * valorHora
      horasExtrasLaboradas = horas - 40
      valorHoraExtra = horasExtrasLaboradas * (valorHora * 1.5)
      sueldoBruto = (valorHora * 40)+valorHoraExtra
    return sueldoBruto

  def parafiscales():

    paraFiscales = salario() *0.09
    return paraFiscales

  def prima():

    prima = salario() * 0.0833
    return prima

  def cesantias():
      cesantia = salario() * 0.0833
      return cesantia

  def intCesantia():
    interesCesantia = salario() * 0.01
    return interesCesantia

  def salud():
    salud = salario() * 0.04
    return salud

  def pension():
    pension = salario()*0.04
    return pension

  def totalDescuento():
    totalDescuentos =  pension() + salud() + parafiscales()
    return totalDescuentos

  def vacaciones():
    vacaciones = salario() * 0.0417
    return vacaciones

  def sueldoNeto():
    sueldoNetoTotal = salario()-totalDescuento()
    return sueldoNetoTotal

    #print("\n\t\t Programa Principal")

  informacion()
  if horas > 40:
    horaExtra = (horas - 40) * valorHora * 1.5
    salarioSinHorasExtras = 40 * valorHora
  else:
    salarioSinHorasExtras = horas * valorHora
    horaExtra = 0

  print("\n\t\t Programa Principal")

  print("\tEl salario sin horas extras es: $",salarioSinHorasExtras)
  print("\tEl salario con horas extras es: $", horaExtra)
  print("\tEl salario bruto es: $", salario())
  print("\tDescuento por parafiscales es: $", parafiscales())
  print("\tDescuento por salud es: $", salud())
  print("\tDescuento por pension es: $", pension())
  print("\tTotal de los descuentos: $", totalDescuento())
  print("\t----------------------------------------------")
  print("\tSueldo neto a pagar: $",sueldoNeto())
  print("\tPrima: $", prima())
  print("\tCesantias: $",cesantias())
  print("\tIntereses de las cesantias: $",intCesantia())
  print("\tVacaciones: $",vacaciones())
  print("\t---------------------------------------------")

  personaNueva = input("\tDesea inscribir la nomina de otro docente si/no: ")

print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tReto 2")

"""
Una Universidad colombiana asesorada por la Universidad El Bosque y siguiendo su mismo espíritu de ayuda a las clases menos favorecidas, ha diseñado un esquema de porcentajes de ayuda (descuento sobre la matrícula) para sus nuevos estudiantes que funciona de la siguiente manera:


*   Cada estudiante candidato deberá dar su nombre y apellidos, su edad en años, el puntaje obtenido en el examen y el número decimal de salarios mínimos mensuales que tiene de ingreso familiar.
*   Presentar un examen de aptitud académica y razonamiento, calificado en números enteros de 0 a 100.

Cálculo del porcentaje de apoyo según los siguientes criterios:
*   Si la edad está en el rango 15 a 18 años dar 25%, de 19 a 21 años dar 15% y de 22 a 25 años dar 10%, para mayores de 25 no dar ningún apoyo por edad.
*    Si el ingreso familiar es inferior o igual a un salario mínimo dar 30%, si es mayor a un salario mínimo e inferior o igual a 2 salarios mínimos dar 20%, si es mayor a dos salarios mínimos e inferior o igual a 3 salarios mínimos dar 10%, si es mayor a tres salarios mínimos e inferior o igual a 4 salarios mínimos dar 5%, para ingresos superiores no dar ningún apoyo por ingreso familiar.
*   Si puntaje de ingreso es mayor o igual a 80 y menor de 86 dar 30%, si es mayor o igual a 86 y menor de 91 dar 35%, si es mayor o igual a 91 y menor de 96 dar 40%, si es mayor o igual a 96 dar 45%. Para puntajes menores de ochenta no hay apoyo por puntaje de examen.
*   Los apoyos recibidos por edad, por ingreso familiar y por puntaje de examen se deben sumar para dar el porcentaje total de apoyo que recibirá el beneficiario, es decir, el porcentaje de descuento sobre el valor de la matrícula.

El dueño de la Universidad le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python que le permita:


*   Leer desde el teclado el nombre y apellido del candidato, su edad entera en años, el puntaje obtenido en el examen y el número decimal de salarios mínimos mensuales de su ingreso familiar.
*   Calcular el valor total de descuento del candidato según los criterios antes definidos.
*   Mostrar en consola el nombre y apellido del beneficiario, el descuento recibido por edad, el recibido por el ingreso familiar, el recibido por el puntaje del examen y el descuento total que recibirá sobre el valor de la matrícula."""

nuevoCandidato = "si"

while nuevoCandidato == "si":
  #Se inicia el programa pidiendo los datos que se necesitan como lo son el nombre, apellido, la edad, el puntaje y los ingresos
  #Entradas
  nombre = input("\tDigite el nombre del candidato: ")
  apellido = input("\tDigite el apellido del candidato: ")
  edad = int(input("\tDigite el edad en años del candidato: "))
  puntaje = float(input("\tDigite el puntaje en la prueba recuerde que el puntaje va de (0 a 100): "))
  if (puntaje < 0) or (puntaje > 100):
    print("\tPuntaje no valido")
    puntaje = float(input("\tDigite el puntaje en la prueba recuerde que el puntaje va de (0 a 100): "))
  ingresos = float(input("\tDigite el número de SMLV del ingreso familiar: "))
  
  #Se inicia el proceso que realiza las respectivas comparaciones para definir cual es el subsidio que corresponde de acuerda a la edad, el puntaje y los ingresos
  if (edad >= 15) and (edad <= 18):
    subsidio1 = 20
  elif (edad >= 19) and (edad <= 21):
    subsidio1 = 15
  elif (edad >= 22) and (edad <= 25):
    subsidio1 = 10
  else:
    subsidio1 = 0
  
  if (ingresos <= 1):
    subsidio2 = 30
  elif (ingresos > 2) and (ingresos <= (3)):
    subsidio2 = 20
  elif (ingresos > (3)) and (ingresos <=  (4)):
    subsidio2 = 10
  elif (ingresos > (4)) and (ingresos <= (5)):
    subsidio2 = 5
  else:
    subsidio2 = 0

  if (puntaje < 80):
    subsidio2 = 0
  elif (puntaje >= 80) and (puntaje < 86):
    subsidio3 = 30
  elif (puntaje >= 86) and (puntaje < 91):
    subsidio3 = 35
  elif (puntaje >= 91) and (puntaje < 96):
    subsidio3 = 40
  elif (puntaje >= 96) and (puntaje <= 100):
    subsidio3 = 45

  #Se calcula el subsidio total que recibira el candidato
  subsidioTotal = (subsidio1 + subsidio2 + subsidio3)
  
  nuevoCandidato = input("\tDesea inscribir un nuevo candidato (si / no): ")

  #Salidas
  #Se imprimen el nombre y apellido el candidato, el subsidio por edad, el subsidio por ingresos familiares y el subsidio por el puntaje obtneido en el examen
  print("\tEl nombre completo del candidato es: ", nombre, apellido)
  print("\tEl descuento por edad a recibir es: ", subsidio1, "%")
  print("\tEl descuento por ingresos familiares a recibir es: ", subsidio2, "%")
  print("\tEl descuento por el puntaje obtenido en el examen a recibir es: ", subsidio3, "%")
  print("\tEl descuento que recibira el candidato", nombre, apellido, " es: ", subsidioTotal,"%")


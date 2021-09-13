print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tMuchos bancos y cajas de ahorro calculan los intereses de las cantidades depositadas por los clientes diariamente según las premisas siguientes. Un capital de 1.000 euros, con una tasa de interés del 6 por 100, renta un interés en un día de 0,06 multiplicado por 1.000 y dividido por 365. Esta operación producirá 0,16 euros de interés y el capital acumulado será 1.000,16. El interés para el segundo día se calculará multiplicando 0,06 por 1.000 y dividiendo el resultado por 365. Diseñar un algoritmo que reciba tres entradas: el capital a depositar, la tasa de interés y la duración del depósito en semanas, y calcular el capital total acumulado al final del período de tiempo especificado.")

print("\tBienvenido al Banco Amigo")
capital = int(input("\tDigite el capital que desea ahorrar: $"))
tasaInteres = float(input("\tDigite la tasa de intereses: "))
semanas = int(input("\tDigite la cantidad de semanas que desea realizar el ahorrar: "))

meses = semanas*15/52
años = meses/12
totalCapital = capital * ( 1 + tasaInteres)**años

print("\tEl capital total acumulado en: ",semanas, "es de: ",totalCapital)

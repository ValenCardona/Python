print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tReto 1 caso 1")

totalPantalon = 0
totalCamisa = 0
totalCamiseta = 0
totalCamisaCuello = 0
totalParMedias = 0
cod1 = 123
cod2 = 345
cod3 = 456
prenda1 = "\tPantalones"
prenda2 = "\tCamisa Manga corta"
prenda3 = "\tCamiseta polo"
prenda4 = "\tCamisa cuello redondo"
prenda5 = "\tPar de medias "
producto = "si"

while producto == "si":
  
  print("\tCodigos: 123, 345, 456")
  cod = int(input("\tDigite el codigo de la prenda a facturar: "))

  if(cod != 123) and (cod != 345) and (cod != 456):

    print ("\tEl codigo ingresado no es valido")
    cod = int(input("\tDigite el codigo de la prenda a facturar: "))

    if (cod == 123):
        cant1 = int(input("\tDigite la cantidad de pantalones: "))
        valorUni1 = 45000
        totalPantalon = cant1 * valorUni1
               
    elif (cod == 345):

        cant2 = int(input("\tDigite la cantidad de camisa manga corta: "))
        valorUni2 = 35000
        totalCamisa = cant2 * valorUni2
        
    elif (cod == 456):

        cant3 = int(input("\tDigite la cantidad de camisetas polo: "))
        valorUni3 = 27000
        totalCamiseta = cant3 * valorUni3
        
  else:
      if (cod == 123):
        cant1 = int(input("\tDigite la cantidad de pantalones: "))
        valorUni1 = 45000
        totalPantalon = cant1 * valorUni1
        
      elif (cod == 345):

        cant2 = int(input("\tDigite la cantidad de camisa manga corta: "))
        valorUni2 = 35000
        totalCamisa = cant2 * valorUni2
        
      elif (cod == 456):

        cant3 = int(input("\tDigite la cantidad de camisetas polo: "))
        valorUni3 = 27000
        totalCamiseta = cant3 * valorUni3

  nuevoProducto = input("\tDesea inscribir un producto que no tiene codigo (si / no): ")

  while nuevoProducto == "si":

    print("\t Nombres: camisa cuello redondo o Par de medias")
    nombre = input("\tDigite el nombre del producto: ")

    productoCorrecto = 0

    if (nombre == "camisa cuello redondo") or (nombre == "Camisa cuello redondo"):

      cant4 = int(input("\tDigite la cantidad de camisas cuello redondo: "))
      valorUni4 = 12000
      totalCamisaCuello = cant4 * valorUni4
      productoCorrecto = 1

    elif ( nombre == "Par de medias ") or (nombre == "par de medias"):

      cant5 = int(input("\tDigite la cantidad de pares de medias: "))
      valorUni5 = 3000
      totalParMedias = cant5 * valorUni5
      productoCorrecto = 1

    if (productoCorrecto == 0):

      print("\tEl producto no existe")

      nombre = input("\tDigite el nombre del producto: ")
      productoCorrecto = 0

      if (nombre == "camisa cuello redondo") or (nombre == "Camisa cuello redondo"):
          cant4 = int(input("\tDigite la cantidad de camisas cuello redondo: "))
          valorUni4 = 12000
          totalCamisaCuello = cant4 * valorUni4
          productoCorrecto = 1

      elif ( nombre == "Par de medias") or (nombre == "par de medias"):

          cant5 = int(input("\tDigite la cantidad de pares de medias: "))
          valorUni5 = 3000
          totalParMedias = cant5 * valorUni5
          productoCorrecto = 1


    nuevoProducto = input ("\tDesea continuar con la facturación de productos sin codigo (si/no): ")

  producto = input ("\tDesea continuar con la facturación de productos con codigos (si/no): ")

subTotal = totalPantalon + totalCamisa + totalCamiseta + totalCamisaCuello + totalParMedias
iVa = 19
iva = 19/100
total = (subTotal * iva) + subTotal
if totalPantalon == 0:
  print("\t No se registro ningun pantalon")
else:
  print ("\tcódigo: ", cod1, " Descripción: ", prenda1, " cantidad: ", cant1, " Valor unitario: ", valorUni1, " Total: ", totalPantalon)
if totalCamisa == 0:
  print("\t No se registro ningun camisa manga larga")
else:
  print ("\tcódigo: ", cod2, " Descripción: ", prenda2, " cantidad: ", cant2, " Valor unitario: ", valorUni2, " Total: ", totalCamisa)
if totalCamiseta == 0:
  print("\t No se registro ningun camiseta tipo polo")
else:
  print ("\tcódigo: ", cod3, " Descripción: ", prenda3, " cantidad: ", cant3, " Valor unitario: ", valorUni3, " Total: ", totalCamiseta)
if totalCamisaCuello == 0:
  print("\t No se registro ningun camisa cuello redondo")
else:
  print ("\tDescripción | ", prenda4, " | Cantidad | ", cant4, " Valor unitario: ", valorUni4, " | Total a pagar de la prenda | ", totalCamisaCuello)
if totalParMedias == 0:
  print("\t No se registro ningun par de medias")
else:
  print ("\tDescripción | ", prenda5, " |Cantidad | " , cant5, " Valor unitario: ", valorUni5, " |Total a pagar de la prenda | ", totalParMedias)
print ("\t--------------------------------------------------------------------------------------")    
print ("\tEl subtotal a pagar es: ", subTotal)
print ("\tEl iva de la compra es: ", iVa, "%")
print ("\tEl total a pagar es: $",total) 

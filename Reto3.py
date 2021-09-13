print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tReto 3")

contDiaserror = 0
contDiasError1= 0
contDiasError2 = 0
contDiasError3 = 0
contDiasBien = 0
contDia = 1
contDiasBien1  = 0
contDiasBien2  = 0
temperatura1 = 0
temperatura2 = 0
diaNuevo = "si"

while diaNuevo == "si":

    #Entradas
    temperaturaMin = float(input("\tDigite la temperatura minima del día: "))
    temperaturaMax = float(input("\tDigite la temperatura maxima del día: "))

    temperatura = [temperaturaMin, temperaturaMax]
    #Salida del ciclo
    if temperatura == [0,0]:
        print("\t\tFin de la salida de campo")
        contDia = contDia - 1
        break
    
    else:
        print("\tLa temperatura del día ",contDia, "es: ", temperatura)
        #Proceso
        if (temperaturaMin >= 5) and (temperaturaMax <= 35):

            if (temperaturaMin >= 5):

                temperatura1 = temperatura1 + temperaturaMin
                contDiasBien1 = contDiasBien1 +1
                
            if (temperaturaMax <= 35):
                temperatura2 = temperatura2 + temperaturaMax
                contDiasBien2 = contDiasBien2 +1

            contDiasBien = contDiasBien +1
            
        if (temperaturaMin < 5) or (temperaturaMax > 35):
            
            print("\tEl día",contDia,"tuvo un error en la toma de sus datos")
            if (temperaturaMin < 5) and (temperaturaMax > 35):

                print("\tEl error estuvo en las dos temperaturas: ", "(",temperaturaMin, ",", temperaturaMax,")")
                contDiasError3 = contDiasError3 + 1
            else:
                    
                if(temperaturaMin < 5):

                    contDiasError1 = contDiasError1 + 1
                    print("\tEl error estuvo en la temperatura minima", temperaturaMin)
                
                if(temperaturaMax > 35):

                    contDiasError2 = contDiasError2 +1
                    print("\tEl error estuvo en la temperatura maxima", temperaturaMax)

            contDiaserror = contDiaserror +1

        contDia = contDia + 1
        
if contDia == 0:
    porcentajError = 0
else:
    porcentajError = (contDiaserror * 100)/contDia

if contDiasBien == 0:
    mediaMenortem = 0
    mediaMayorTem = 0
else:
    mediaMenortem = temperatura1 / contDiasBien
    mediaMayorTem = temperatura2 / contDiasBien
    
#Salidas
print("\n\tEl total de días registrados son: ", contDia)
print("\n\tEl total de días que tuvieron error son: ", contDiaserror)
print("\n\tEl total de días en que las temperaturas fueron menores a 5°C fueron: ",contDiasError1)
print("\n\tEl total de días en que las temperaturas fueron mayores a 35°C fueron: ",contDiasError2)
print("\n\tEl total de días en las que ambas temperaturas tuvieron errores fueron: ",contDiasError3)
print("\n\tLa temperatura media minima de los datos sin tener encuenta los días de error es: ", mediaMenortem, "°C")
print("\n\tLa temperatura media mayor de los datos sin tener encuenta los días de error es: ", mediaMayorTem, "°C")
print("\n\tEl porcentaje de los días que tuvieron errores es: ", porcentajError, "%")
   

        

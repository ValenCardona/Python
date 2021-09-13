print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \nMenu")

reiniciar = "si"
while reiniciar == "si":
    print ("\n\t\t Menú Codgigo realizados")
    print ("\n\t 1. Operaciones Matemáticas")
    print ("\n\t 2. Área del Triángulo")
    print ("\n\t 3. Longitud y área del círculo")
    print ("\n\t 4. Salario semanl de un trabajador")
    print ("\n\t 5. Liquidación de Intereses")
    print ("\n\t 6. Liquidación compra de productos")
    print ("\n\t 7. Jerarquía de operadores")
    print ("\n\t 8. Nomina")
    
    print ("\n\t 9. Sistema Americano de calificaciones")
    print ("\n\t 10. Estadisticas Peso")
    print ("\n\t 11. Caracterización de los números por medio de ciclos (While y for)")
    print ("\n\t 12. Cadena")
    print ("\n\t 13. Ejercicio de suma de elementos positivos y negativos en una matriz nxm")
    print ("\n\t 14. Actividad archivos")
    print ("\n\t 15. Diccionarios")
     
    print ("\n\t 16. Reto 1: Factura de caja")
    print ("\n\t 17. Reto 2: Descuento en Matricula")
    print ("\n\t 18. Reto 3: Toma de datos en una salida de campo")
    print ("\n\t 19. Reto 4: Nomina de un docente")
    print ("\n\t 20. Reto 5: Agenda")
    
 #Entradas
    opcion = int(input("\n\tDigite el número del programa que desea ejecutar de 1 a 20: "))

    if opcion < 1 or opcion > 20:
        print("\t La opción seleccionada no es valida")
        opcion = int(input("\n\tDigite el número del programa que desea ejecutar de 1 a 20: "))

    elif opcion == 1:
        from Operaciones_basicas import *
        reiniciar =input("\tDesea volver al Menú principal si/no : ")
     
    elif opcion == 2:
         from Area import *
         reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 3:
        from Longitud_y_area import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 4:
        from Tarifa_de_un_trabajador import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 5:
        from Capital import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 6:
        from Factura import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 7:
        from Operaciones_matematicas import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 8:
        from Nomina import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 9:
        from CaracterizacionNotas import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 10:
        from Encuesta_Peso import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 11:
        from Caracterizacion_de_numeros import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 12:
        from Cadena import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 13:
        from Listas_y_matrices import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 14:
        from Archivos import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 15:
        from Diccionarios import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 16:
        from Reto1 import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 17:
        from Reto2 import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 18:
        from Reto3 import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 19:
        from Reto4 import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

    elif opcion == 20:
        from Reto5 import *
        reiniciar =input("\tDesea volver al Menú principal si /no : ")

print("\n\t\t Fin del Programa")

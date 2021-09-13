print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tSistema Americano de Calificaciones")

contA = 0 
contB = 0 
contC = 0 
contD = 0
contF = 0

#Entradas
cantEstudiantes = int(input("\n\t Señor usuario, Digite el numero de estudiantes a analizar:   "))
#Procesos       
for contEstudiantes in range (0, cantEstudiantes):
    calificacion = float(input("\n\t Digite la nota del estudiante:   "))        
    if(calificacion >=90 and calificacion <=100):
        contA =contA + 1
    elif(calificacion <90 and calificacion >=80):
        contB =contB + 1
    elif(calificacion <80 and calificacion >=70):
        contC =contC + 1
    elif(calificacion <70 and calificacion >=60):
        contD =contD + 1
    else:
        contF = contF + 1
                
       
#Salidas
print ("\n\t\t Resultados del Proceso Academico de Programacion Python")
print ("\n\t\t Numero total de Estudiantes=", cantEstudiantes)
print ("\n\t\t Estudiantes con Nota A: ", contA)
print ("\n\t\t Estudiantes con Nota B: ", contB)
print ("\n\t\t Estudiantes con Nota C: ", contC)
print ("\n\t\t Estudiantes con Nota D: ", contD)
print ("\n\t\t Estudiantes con Nota F: ", contF)





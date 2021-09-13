print("\t Valentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tReto 5")
"""
El director del Programa de Ingeniería de Sistemas de la Universidad El Bosque, a raíz de la
participación en un proyecto muy especial con el MinTic, requiere poder generar una agenda
con los datos de nombre y apellido, número de cédula y el número celular de todos los
beneficiarios del proyecto, para poder hacerles algún seguimiento en su proceso de formación.
Dicha agenda deberá ser almacenada en un archivo de texto en el directorio activo con el
nombre agenda.txt. Cada beneficiario ocupará tres líneas en el archivo, una por cada campo
(nombre y apellido, cedula, celular). Por ejemplo, el beneficiario José Castro con cédula
18145321 y celular 3091234567 y la beneficiaria Sofía Vergara con cédula 52120318 y celular
3109876543, quedarían así en el archivo:

José Castro
18145321
3091234567
Sofía Vergara
52120318
3109876543

El director del Programa de Ingeniería de Sistemas le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python que le permita:
• Crear el archivo agenda.txt leyendo los datos desde el teclado (por lo menos 10 beneficiarios).
• Buscar en el archivo agenda.txt el número celular de un beneficiario, dados su nombre y apellido.
• Añadir un nuevo beneficiario en la agenda.txt, al final del archivo. No debe haber otro beneficiario con la misma cédula.
• Borrar un beneficiario de la agenda.txt dado su número de cédula.
• Buscar, añadir y borrar un beneficiario deberán ser funciones, que serán llamadas dentro del programa principal.
• Mostrar en consola el listado completo de los beneficiarios del archivo agenda.txt.
• Mostrar en consola el listado de los beneficiarios cuyo nombre empieza por una letra determinada.
• Presentar un menú con las diferentes opciones solicitadas para que el usuario pueda decidir qué proceso desea realizar.

"""
import os
import io

def escribirAgenda():
    with open("archivo.txt","w", encoding = "utf-8") as doc:
        for i in beneficiario:
            doc.write("{}\n".format(i[0]))
            doc.write("{}\n".format(i[1]))
            doc.write("{}\n".format(i[2]))
            
def imprimir(beneficiario):
    print("\tListado de beneficiarios ")
    archivoTexto = open ("archivo.txt", "r")
    beneficiario = archivoTexto.readlines()
    for cedula in beneficiario:
        print(cedula)
    archivoTexto.close()

def listadoFiltrado(beneficiario):
    archivoTexto = open ("archivo.txt", "r")
    letra = input ("\tDigite la letra por la que empiezan los beneficiarios: ")
    print("\tListado filtrado de beneficiarios:")
    #usuario = archivoTexto.readlines()
    n = 0
    for i in range(len(beneficiario)):
        nombre1 = beneficiario[i][0]
        if nombre1[0:1].lower() == letra.lower():
            print(beneficiario[i][0], "\n", beneficiario[i][1], "\n", beneficiario[i][2])
            n += 1
    if n == 0:
        print("\tLa letra", letra, "no existe")

    archivoTexto.close()

    
def cargar(beneficiario):
    print("\tDigite la información del beneficiario a agregar: ")
    archivoTexto = open ("archivo.txt", "a")
    nombre = input("\tIngrese el nombre completo del beneficiario: ")
    cedula = input("\tIngrese la cédula del beneficiario: ")
    numeroCelular = input("\tIngrese el teléfono celular del beneficiario: ")
    index = None
    for x in range(len(beneficiario)):
        if beneficiario[x][1] == cedula:
            index = x
            break
    if index != None:
       print("\tEl numero de cedula ya existe") 
    else:
        beneficiario.append ([nombre, cedula, numeroCelular])
        escribirAgenda()
        print("\tEl beneficiario ha sido agregado")
    
def buscar(beneficiario):
    nombre = input("\tDigite el nombre y apellido del beneficiario a buscar: ")
    archivoTexto = open ("archivo.txt", "r")
    nuevoNombre = True
    for i in range(len(beneficiario)):
        if(nombre.lower() == beneficiario[i][0].lower()):
            print(beneficiario[i][0], "\n", beneficiario[i][1], "\n", beneficiario[i][2])
            nuevoNombre = False
            break
    if nuevoNombre == True:
        print("\t El beneficiaro no existe", nombre)
    archivoTexto.close()

def borrar(beneficiario):
    contenido = []
    archivoTexto = open("archivo.txt", "r")
    beneficiario = archivoTexto.readlines()
    for linea in beneficiario:
        contenido.append(linea.strip("\n"))
    archivoTexto.close
    
    cedula = input("\tDigite la cedula del beneficiario a borrar:")
    indiceCedula = contenido.index(cedula)

    del contenido[(indiceCedula - 1) : (indiceCedula + 2)]
    archivoTexto = open("archivo.txt", "w")
    for i in contenido:
        archivoTexto.write(i + "\n")
    archivoTexto.close()
    print("\tEl usuario ha sido eliminado del listado")
# MENÚ PRINCIPAL

beneficiario =[]
reiniciar = "s"
while reiniciar == "s":
    print ("\n\t Menu Principal\n")
    print ("\n\t 1. Ver listado\n")
    print ("\n\t 2. Ver listado filtrado\n")
    print ("\n\t 3. Agregar beneficiario\n")
    print ("\n\t 4. Buscar beneficiario\n")
    print ("\n\t 5. Borrar beneficiario\n")
    print ("\n\t 6. Salir\n")

 
    #Entradas
    opcion = int(input("\tDigite una opción del menu: "))
    
    #Procesos
    if opcion < 1 or opcion > 6:
        print ("\n\t Opcion no disponible en el menu")
    elif opcion == 1:
        imprimir(beneficiario)
    elif opcion == 2:
        listadoFiltrado(beneficiario)
    elif opcion == 3:
        cargar(beneficiario)
    elif opcion == 4:
        buscar(beneficiario)
    elif opcion == 5:
        borrar(beneficiario)
    elif opcion == 6:
        break
    reiniciar = "s"
print ("\tHasta pronto")
##archivo_texto = open ("archivo2.txt","r")
##letra = input("Digite la inical del nombre ")
##for linea in archivo_texto:
##    if(linea.startswith(letra)):
##        print (linea)

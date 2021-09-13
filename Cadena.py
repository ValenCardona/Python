print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tMetodos de Cadenas")

reiniciar = "si"

while reiniciar == "si":

    print ("\n\t\t Universidad El Bosque - Misión TIC")
    print ("\n\t\t Aplicacion con metodos de cadenas")

    cadena = input("Digite una secuencia de caracteres: ")
    tamaño = len(cadena)

    print("\n\t\t El tamaño de la cadena es: ", tamaño)

    #Recorrido de la cadena por medio de bucles
    
    for contador in  range (0,tamaño):

        letra = cadena[contador]

        print("\n\t Posición [",contador,"] = ", letra)

    for contador in cadena:

        print("\n\t", contador)

    indice = 0
    while indice < tamaño:
        letra = cadena[indice]
        print('\n\t', letra, '\n')
        indice = indice +1

    #Rebanado de una cadena
        
    print("\t Imprimir los tres primeros datos de la cadena ", cadena[0:3])
    print("\t Imprimir los tres primeros datos de la cadena ", cadena[:3])
    print("\t Imprimir desde el quinto dato de la cadena hasta el final ", cadena[5:])
    print("\t Imprimir los ultimos tres caracteres de la cadena ", cadena[:-3])
    
    #Las cadenas son inmutables

    mensaje = '\tHola Mundo'
    nuevoMensaje = mensaje[:5] +'Profesor' 
    print('\tMensaje inicial', mensaje)
    print('\t', nuevoMensaje)

    #Iterando y contando

    palabra = '\tMisión TIC'
    contador = 0

    for letra in palabra:
        if letra == 'i':
            contador = contador + 1
    print('\t',contador)

    #El operador in

    'i' in '\tMisión TIC'

    #Comparación de cadenas

    palabra = input("\tDigite una fruta ")

    if palabra < 'mango':

        print('\tTu fruta', palabra, ', esta antes de mango')

    elif palabra > 'mango':

       print('\tTu fruta', palabra, ', esta despues de mango')

    else:
        print('\tMuy bien, mango')

    #Metodos de cadenas

    cosa = '\tcelular'
    print('\t',cosa)
    print ('\t',type(cosa))
    print ('\t',dir(cosa))
    
    #1

    palabra = '\tBienvenido a la universidad el bosque'
    nuevaPalabra = palabra.upper()
    print ('\t', nuevaPalabra)

    #2

    palabra.find('uni')
    palabra.find('uni', 3)

    #3

    frase = '\tEste es un programa de metodos de cadenas'
    frase.strip()

    #4 startswith

    linea = '\tFeliz dia'
    print ('\t',linea)
    linea.startswith('Feliz')
    linea.lower().startswith('f')

    #Analizando cadenas

    info = '\tvalencardona1308@gmail.com Sabado 5 de Junio'
    print ('\t',info)
    arroba = info.find('@')
    print ('\t', arroba)

    espacio = info.find(' ', arroba)
    print ('\t', espacio)

    direccion = info [arroba + 1 : espacio]
    print ( '\t', direccion)

    #depuracion

    while True:
        linea = input('\tDigite el signo # o la palabra fin: ')
        if linea[0] == '#':
            continue
        if linea == 'fin':
            break
        print('\t',linea)
    print('\t¡Terminado!')

    #Metodos principales

    cadena = input("\tDigite una frase: ")
    print ('\t',cadena)
    print("\tEste metodo capitaliza la primera letra de la frase")
    print ("\t", cadena.capitalize())

    print("\tEste metodo convierte una cadena a minusculas")
    print ("\t", cadena.lower())

    print("\tEste metodo convierte una cadena a mayusculas")
    print("\t", cadena.upper())
    
    print("\tEste metodo convierte mayusculas a minusculas y viceversa")
    print ("\t", cadena.swapcase())

    print("\tEste metodo convierte una cadena en formato titulo")
    print ("\t", cadena.title())

    print("\tEste metodo centra una cadena de texto")
    print ("\t", cadena.center(50, "*"))

    print("\tEste metodo alinea la cadena de texto a la izquierda")
    print ("\t", cadena.ljust(50, "*"))

    print("\tEste metodo alinea la cadena de texto a la derecha")
    print ("\t", cadena.rjust(50, "*"))

    numero = int(input("\tDigite un numero: "))
    print ('\t',numero)
    print("\tEste metodo rellenar un texto anteponiendo ceros")
    print ("\t", str(numero).zfill(12))

    print ('\t',cadena)
    print("\tEste metodo cuenta la cantidad de apariciones de una sub cadena")
    print ("\t", cadena.count("a"))

    cadena1 = "\tbienvenido a mi aplicación"
    print ("\t", cadena1.capitalize())
    print("\tEste metodo busca ina subcadena dentro de una cadena")
    print ("\t", cadena1.find("mi", 0, 10))

    print("\tEste metodo se encarga de saber si una cadena comienza con una subcadena determinada")
    print ("\t", cadena1.startswith("Bienvenido"))
    print ("\t", cadena1.startswith("aplicación"))
    print ("\t", cadena1.startswith("aplicación", 16))

    print("\tEste metodo se encarga de saber si una cadena finaliza con una subcadena predterminada")
    print ("\t", cadena1.endswith("aplicación"))
    print ("\t", cadena1.endswith("Bienvenido"))
    print ("\t", cadena1.endswith("Bienvenido", 0, 10))

    cadena2 = "\tHola mundo, hoy es 4 de Junio"
    print ("\tLa cadena 2 es: ", cadena2)
    cadena3 = "\tJunio4de2021"
    print ("\tLacadena 3 es: ",cadena3)
    print ("\tEste metodo se encarga de saber si la cadena es alfanumerica")
    print ("\t", "La cadena 2 es ", cadena2.isalnum())
    print ("\t", "La cadena 3 es ", cadena3.isalnum())

    cadena4 = "\tWelcome To Colombia"
    print("\tLa cadena 4 es: ", cadena4)
    print("\tEste metodo se encarga de saber si una cadena es alfabetica")
    print("\t", "La cadena 2 es ", cadena2.isalpha())
    print("\t", "La cadena 3 es ", cadena3.isalpha())
    print("\t", "La cadena 4 es ", cadena4.isalpha())

    cadena5 = "2021"
    print ("\tLa cadeba 5 es : ", cadena5)
    print("\tEste metodo se encarga de saber si una cadena es numerica")
    print("\t", "La cadena 2 es ", cadena2.isdigit())
    print("\t", "La cadena 3 es ", cadena3.isdigit())
    print("\t", "La cadena 4 es ", cadena4.isdigit())
    print("\t", "La cadena 5 es ", cadena5.isdigit())

    cadena6 = "\tfeliz día"
    print("\tLa cadeba 6 es : ", cadena6)
    print("\tEste metodo se encarga de saber si una cadena contiene solo minusculas")
    print("\tLa cadena 2 es ", cadena2.islower())
    print("\tLa cadena 3 es ", cadena3.islower())
    print("\tLa cadena 4 es ", cadena4.islower())
    print("\tLa cadena 6 es ", cadena6.islower())

    cadena7 = "\tBIENVENIDOS A JUNIO"
    print("\tLa cadeba 7 es : " ,cadena7)
    print("\tEste metodo se encarga de saber si una cadena contiene solo mayusculas")
    print("\t", "La cadena 2 es ", cadena2.isupper())
    print("\t", "La cadena 3 es ", cadena3.isupper())
    print("\t", "La cadena 4 es ", cadena4.isupper())
    print("\t", "La cadena 7 es ", cadena7.isupper())

    cadena8 = " "
    print("\tLa cadeba 8 es : ", cadena8)
    print("\tEste metodo se encarga de saber si una cadena contine algun espacio")
    print("\t", "La cadena 2 es ", cadena2.isdigit())
    print("\t", "La cadena 3 es ", cadena3.isdigit())
    print("\t", "La cadena 4 es ", cadena4.isdigit())
    print("\t", "La cadena 8 es ", cadena8.isdigit())

    print("\tEste metodo se encarga de saber si una cadena tiene formato de titulo")
    print("\t", "La cadena 2 es ", cadena2.istitle())
    print("\t", "La cadena 3 es ", cadena3.istitle())
    print("\t", "La cadena 4 es ", cadena4.istitle())
    print("\t", "La cadena 5 es ", cadena5.istitle())

    buscar =  "\tnombre apellido edad"
    informacion = "\tValentina Cardona Ligarreto 20 años"
    print("\tste metodo se encarga de buscar y reemplaza el texto en una cadena")
    print ("\t", "Estimada Sra. nombre apellido edad:".replace(buscar, informacion))

    cadena9 = " \twww.aulavirtual.unbosque.edu.co."
    print ("\tEste metodo elimina caracteres a la izquierda y a la derecha")
    print ("\t", cadena9.strip('.'))
    print ("\tEste metodo elimina caracteres a la izquierda")
    print ("\t", cadena9.lstrip('.'))
    print ("\tEste metodo elimina caracteres a la derecha")
    print ("\t", cadena9.rstrip('.'))

    numFact = ("\tN° 0000-0", "-0000(ID: ", ")")
    numero = "1254"
    facturaNum = numero.join(numFact)
    print("\t", facturaNum)

    cadena10 = "\tBienvenidoTripulanteMisión TIC 2022".partition("Tripulante")
    print("\tEste metodo se encarga de partir una cadena en tres partes")
    print("\t", cadena10)

    palabras = "\tpython, java, c++, HTLM, CSS, Assembler"
    print ("\tEste metodo parte una cadena en varias partes utilizando separadores")
    print ("\t", palabras.split(","))

    palabras = "\tpython java c++ HTLM CSS Assembler"
    print("\tEste metodo parte una cadena en lineas")
    print("\t", palabras.splitlines())
    
    reiniciar = input("\tDesea realizar una nueva cadena (si/no): ")     

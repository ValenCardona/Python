print ("\tValentina Cardona Ligarreto \n\tMisión TIC 2022 \n\tUniversidad El Bosque \n\tDiccionarios")

print ("\n\t\tPasos para crear un diccionario")

print ("\tPaso 1 - Crear una diccionario vacio")
diccionario = dict ()

print ("\tPaso 2 – Definir los datos de entrada el diccionario")
documento = int(input("\tDigite el documento de la persona: "))
nombre = input("\tDigite el nombre de la persona: ")
edad = int(input("\tDigite la edad de la persona: "))
peso = float(input("\tDigite el peso de la persona: "))

print ("\tPaso 3 – definir la clave (Variable que va a manipular el diccionario) & Paso 4 – Ingresar la información en el diccionario desde teclado")
pesos = {}
pesos[documento]=(nombre, edad, peso)

print ("\tPaso 5 - Visualizar la información del diccionario")
print ("\t", pesos)

print ("\t Paso 6 - Visualizar la información del diccionario posición por posición")

documento = int(input("\tIngrese el documento de la persona a consultar:"))
if(documento in pesos):
      print("\t", pesos[documento][0],pesos[documento][1],pesos[documento][2])

print("\t----------------------------------------")
print ("\n\t\tEjemplos de diccionarios")

print ("\t1.")
print ("\n\tAgregar elementos al diccionario vacio")

diccionario = {1: 'hola', 89: 'Pythonista', 'a': 'b', 'c': 27}
print ("\t", diccionario)

print("\n\tImprimir clave y elemento del diccionario")

for clave in diccionario:
    print ("\t", clave, diccionario[clave])

print ("\t2. Mediante funciones generar un diccionario que tenga: codigo, descripción, precio, stock")

def cargar():
    productos={}
    continua="si"
    
    while continua == "si":
        
        codigo=int(input("\tIngrese el codigo del producto:"))
        descripcion=input("\tIngrese la descripcion:")
        precio=float(input("\tIngrese el precio:"))
        stock=int(input("\tIngrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("\tDesea cargar otro producto[si/no]?")
        
    return productos

def imprimir(productos):
    
    print("\tListado completo de productos:")
    print("\t codigo, descripción, producto")
    for codigo in productos:
        print("\t", codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])

#Programa Principal
productos = cargar()
imprimir(productos)

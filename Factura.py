print ("\tValentina Cardona Ligarreto \n Misión TIC 2022 \n Universidad El Bosque \n Se trata de escribir el algoritmo que permita emitir la factura correspondiente a una compra de un artículo determinado, del que se adquieren una o varias unidades. El IVA a aplicar es del 15 por 100.")

codigo = int(input("\tDigite el codigo del articulo: "))
producto = input("\tDigite el nombre del producto: ")
cantidad = int(input("\tDigite la cantidad del articulos:"))
precio = int(input("\tDigite el precio del articulo: $"))
codFactura = int(input("\tDigite el codigo de la factura: "))

subTotal = precio * cantidad
iva = int(subTotal * 0.15)
precioTotal = subTotal + iva

print("\tFactura numero: ",codFactura)
print("\t---------------------------------")
print("\tCodigo producto", "| ", "Descripción", "| ", "Cantidad", "| ", "Precio ", "| ", "Sub total")
print("\t",codigo, "| ", producto, "| ", cantidad, "| ", precio, "| ", subTotal)
print("\t----------------------------------------------------------------")
print("\tIva: ", iva)
print("\t----------------------------------------------------------------")
print("\tValor a pagar es: ", precioTotal)

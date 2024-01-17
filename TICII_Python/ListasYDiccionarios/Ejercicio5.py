# key: value
print("Bienvenid@ a la gestion de facturas")

opc = 1
diccionarioFacturas = {}
"""
Las facturas se almacenarán de la siguiente manera:
key: value
La key será el nº de la factura, y el value será la cuantía de la factura
Ejemplo:
{
"fact1": 1000,
"fact2": 500,
"fact3": 1500
}
"""
while opc != 0:
    print("1. Pagar factura")
    print("2. Anadir factura")
    
    print("0. Terminar")
    opc = int(input("Qué desea hacer?"))
    
    # Lo ideal es iterar sobre las facturas para poder visualizarlas
    # nFactura es la key del diccionario
    for nFactura in diccionarioFacturas:
        print(nFactura+": "+str(diccionarioFacturas[nFactura]))
    
    if opc == 1:
        print("Pagar factura")
    

    

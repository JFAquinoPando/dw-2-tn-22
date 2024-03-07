# 1- En una tienda se ha establecido la siguiente oferta: 
# por compras menores a 100.000 se hace un descuento de 8%, pero para compras a partir de 100.000 el descuento es de 10%. Se pide ingresar la cantidad y el precio del producto que se compra y determinar cuánto se descontará y cuanto se cobrará.

cantidad = int(input("Ingrese la cantidad de su producto: "))
precioProducto = int(input("Ingrese el precio de su producto: "))
montoCompra = precioProducto * cantidad

if montoCompra < 100000:
    descuento = 8/100
else: # elif montoCompra >= 100000:
    descuento = 10/100

seDescontara = montoCompra * descuento
aPagar = montoCompra - seDescontara
print(f"Tu monto de compra alcanza: {montoCompra}")
print(f"Se descontará: {seDescontara}")
print(f"Debe abonar: {aPagar}")


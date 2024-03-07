# 8- En una tienda se efectúa una promoción en la cual se hace un descuento sobre el valor de la cuenta total, según el color de la bolilla que el cliente saque al pagar en caja. 
#Si la bolilla es de color blanco no se hará descuento alguno, si es verde se le hará un 10% de descuento, si es amarilla un 25%, si es azul un 50% y si es roja un 100%. Determinar la cantidad final que el cliente deberá pagar por su compra. Se sabe que sólo hay bolillas de los colores mencionados.

import random
cuentaTotal = int(input("Ingrese por favor su monto de cuenta total: "))
bolilla = random.randint(1,5)

if bolilla == 1:
    color = "blanco"
    descuento = 0
elif bolilla == 2:
    color = "verde"
    descuento = 10
elif bolilla == 3:
    color = "amarillo"
    descuento = 25
elif bolilla == 4:
    color = "azul"
    descuento = 50
elif bolilla == 5:
    color = "rojo"
    descuento = 100

print(f"Sacaste el color {color}, tienes un descuento de {descuento}%")
print(f"Monto total de compra es de {cuentaTotal}")
montoPagar = cuentaTotal - (cuentaTotal * (descuento/100))
print(f"El monto a pagar (con descuento) es: {montoPagar}")

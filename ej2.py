# 2- Una empresa quiere hacer una compra de varias piezas de la misma clase en una fábrica de refacciones. La empresa dependiendo del monto total de la compra decidirá qué hacer para pagar al fabricante. Si el monto total de la compra excede de 500000 la empresa tendrá la capacidad de invertir de su propio dinero un 55% del monto de la compra, pedir prestado al banco un 30% y el resto lo pagará solicitando un crédito al fabricante. 
# Si el monto total de la compra no excede de 500000 la empresa tendrá capacidad de invertir de su propio dinero un 70% y el restante 30% lo pagará solicitando crédito al fabricante. 
# El fabricante cobra por concepto de intereses un 20% sobre la cantidad que se le pague a crédito.

montoCompra = int(input("Ingrese el valor de la compra: "))
if montoCompra > 500000:
    empresa = 55/100
    banco = 30/100
    credito = 1 - (empresa + banco)
    recarga = credito + (credito * (20/100))
else:
    empresa = 70/100
    credito = 30/100
    banco = 0
    recarga = credito + (credito * (20/100))

print(f"Empresa: {empresa * 100}% => {montoCompra * empresa}")
print(f"Banco: {banco * 100}% => {montoCompra * banco}")
print(f"Credito: {credito * 100}% => {montoCompra * credito}")
print(f"Recarga 20% adicional de Credito: {recarga * 100}% => {montoCompra * recarga}")
print(f"Total a devolver: {montoCompra * (empresa + banco + recarga)}")
# 3- Un vendedor recibes tomando encuenta su sueldo base más comisiones. un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que  realiza en el mes y el total que recibirá en el me

sueldo = 2680250

venta1 = int(input("Ingrese el valor de su venta 1: "))
venta2 = int(input("Ingrese el valor de su venta 2: "))
venta3 = int(input("Ingrese el valor de su venta 3: "))

ventas = venta1 + venta2 + venta3
comision = ventas * (10/100)
totalMes = sueldo + comision

print(f"Comisión: {comision}")
print(f"Sueldo + comisión: {totalMes}")


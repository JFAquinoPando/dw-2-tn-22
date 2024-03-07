# 9- Ingresar dos valores en las variables “maximo” y “minimo” y luego ingresar un valor en la variable “temperatura”. Imprime un mensaje si el valor de temperatura no está dentro del rango de marcado por minimo y maximo

maximo = float(input("Ingresa el valor maximo de temperatura: "))
minimo = float(input("Ingresa el valor minimo de temperatura: "))
temperatura = float(input("Ingresa el valor de la temperatura actual: "))

if temperatura >= minimo and temperatura <=maximo:
    print("La temperatura se encuentra dentro del rango")
else:
    print("La temperatura está fuera del rango")

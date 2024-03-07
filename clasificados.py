# He creado un código para emular el sorteo de la
# fase de grupos de la libertadores

# Guardo en una lista los clasificados de la fase de grupos
clasificados = ["Coco Colo", "Nacional PY", "River Plate", "Boca Juniors", "Fluminense", "Libertad", "Palmeiras", "Mineiro", "Racing", "Internacional Porto Alegre", "Sao Paulo", "Estudiantes", "Cerro", "Liga de Quito", "Ind. del Valle", "Sportivo Trinidense"]

# Traigo (importar) la librería para trabajar con los 
# números aleatorios
import random
import time

# Guardo en la variable "posicion" el  valor aleatorio entre 0 y 15
posicion = random.randint(0,15)

print(posicion)
# Muestro quién será el equipo sorteado
print(clasificados[posicion])

# Listado  de enfrentamientos que iré cargando
# para los 8vos de final
enfrentamientos=[]

# Listado de a 2 equipos que se enfrentarán
partido = []

# Mientras la cantidad de equipos en mi listado de 
# clasificados sea mayor a cero, seguiré esta operación
while(len(clasificados)>0):
    # Muestro quién será el equipo sorteado y entre 0 y lo que vaya quedando
    posicion = random.randint(0,len(clasificados)-1)

    # agrego a mi equipo sorteado a la lista de equipos a enfrentarse
    partido.append(clasificados[posicion])

    # Borro al equipo sorteado ya de la lista de clasificados
    del clasificados[posicion]

    # Si ya mi partido tiene a 2 equipos a enfrentarse...
    if(len(partido) == 2):
        # Lo agrego a mi lista de enfrentamientos
        enfrentamientos.append(partido)
        # Y reinicio para un nuevo partido
        partido=[]
print("La composicion queda para los 8vos así:")

numeroPartido = 1
# Voy a imprimir que numero iran teniendo cada par de clubes
for juego in enfrentamientos:
    print(f"Juego {numeroPartido}: {juego}")
    time.sleep(2)
    # Voy incrementando el número de juego
    numeroPartido = numeroPartido + 1

    



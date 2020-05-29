import random

def lee_entero(msg):
    """ Lee un entero proporcionado por el usuario """
    es_entero = False
    while not es_entero:  # False -> not False -> True
        valor = input(msg)
        if valor.isdigit():
            n = int(valor)
            es_entero = True
        else:
            print("Error: el valor proporcionado no es un entero!")
            print("---")

    return n

# 1. Leer valor de n
n = lee_entero("Número de claves a generar n: ")
# 2. Leer valor de m
m = lee_entero("Longitud de las claves m: ")
# 3. Crear lista de n claves de longitud m
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()
digitos = "1234567890"

claves = []
for i in range(n):
    # fabricar una clave
    clave = random.choice(minusculas)  # clave = "d"
    clave = clave + random.choice(mayusculas)  # clave = "dG"
    clave += random.choice(digitos)  # clave = "dG6"
    
    p = m - 3  # clase = "dG6_____" faltan
    for i in range(p):
        clave += random.choice(minusculas + mayusculas + digitos)
    # Rompe patrones
    # ------
    claves.append(clave)
    
# 4. Imprimir lista de claves
for clave in claves:
    print(clave)

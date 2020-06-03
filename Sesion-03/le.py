import os


def obtener_elementos(carp):
    """ Leer la lista de elementos de carp y regresar la lista """
    elementos = []
    
    nombres = os.listdir(carp)
    
    for nombre in nombres:
        tam = os.path.getsize(nombre)
        elem = [nombre, tam]
        elementos.append(elem)
    
    return elementos

def imprime_txt(elems):
    """ Imprime la lista de elementos en formato txt """
    print("{:10}  {}".format("TAMAÑO", "NOMBRE") )
    for e in elems:
        print("{:10}  {}".format(e[1], e[0]) )


carpeta = "."

# Leer lista de elementos con nombre y tamaño
elementos = obtener_elementos(carpeta)

# Ordenar los elementos por nombre
elementos.sort(key=lambda x: x[0].lower() )  # x -> ["nom", 1234], x[0]

# Imprime lista de elementos en formato txt
imprime_txt(elementos)
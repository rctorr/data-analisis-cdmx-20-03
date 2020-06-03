import datetime
import os


def obtener_elementos(carp):
    """ Leer la lista de elementos de carp y regresar la lista """
    elementos = []
    
    nombres = os.listdir(carp)
    
    for nombre in nombres:
        tam = os.path.getsize(nombre)
        fecha = os.path.getmtime(nombre)  # fecha en timestamp o epoc | 1970-01-01
        fecha = datetime.datetime.fromtimestamp(fecha)  # fecha python
        elem = [nombre, tam, fecha]
        elementos.append(elem)
    
    return elementos

def imprime_txt(elems):
    """ Imprime la lista de elementos en formato txt """
    print("{:10}  {:19}  {}".format("TAMAÑO", "FECHA", "NOMBRE") )
    for e in elems:
        fecha = e[2].strftime("%Y-%m-%d %H:%M:%S")
        print("{:10}  {:19}  {}".format(e[1], fecha, e[0]) )


carpeta = "."

# Leer lista de elementos con nombre, tamaño y fecha
elementos = obtener_elementos(carpeta)

# Ordenar los elementos por nombre
# elementos.sort(key=lambda x: x[0].lower() )  # x -> ["nom", 1234], x[0]
# Ordenar los elementos por fecha, el más reciente primeo
elementos.sort(key=lambda x: x[0].lower() )  # x -> ["nom", 1234, "fecha"], x[0]

# Imprime lista de elementos en formato txt
imprime_txt(elementos)
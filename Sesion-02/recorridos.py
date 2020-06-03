def obtener_datos():
    """ Obtiene la lista de recorridos y el total """
    # Obteniendo datos
    recorridos = [
        {  # 0
            "ORIGEN":"Roma Norte",
            "DESTINO":"Tabacalera",
            "TIEMPO":"15:00"
        },
        {  # 1
            "ORIGEN":"Reforma",
            "DESTINO":"Juárez",
            "TIEMPO":"8:00"
        },
        {  # 2
            "ORIGEN":"Alameda",
            "DESTINO":"Condesa",
            "TIEMPO":"20:00"
        },
        {  # 3
            "ORIGEN":"Roma Sur",
            "DESTINO":"Roma Norte",
            "TIEMPO":"4:00"
        },
        {  # 4
            "ORIGEN":"Buenavista",
            "DESTINO":"Del Valle Norte",
            "TIEMPO":"30:00"
        },
    ]
    total = 0
    for r in recorridos:
        minutos = r["TIEMPO"].split(":")[0]  # "30:00" -> ["30", "00"]
        minutos = int(minutos)
        total += minutos
    
    # total = 350 -> "350:00"
    total = str(total) + ":00"

    return recorridos, total

# RETO: Tranforma en una función
# Imprimir lista de recorridos
def imprime_txt(rec, tot):
    """ Imprime la lista de recorridos en formato txt """
    linea = "-" * 60
    formato1 = "{:15} | {:15} | {:10}"  # Formato para encabezado
    formato2 = "{:15} | {:15} | {:>10}"  # Formato para recorridos
    formato3 = "{:15} | {:>15} | {:>10}"  # Formato para total

    print()
    print(linea)
    print(formato1.format(*rec[0].keys() ))  # "ORIGEN", "D", "T"
    print(linea)
    for r in rec:
        print(formato2.format(*r.values()))
    print(linea)
    print(formato3.format("", "Tiempo total:", tot))
    print()


# Ejecutar funcines
rec, tot = obtener_datos()
imprime_txt(rec, tot)

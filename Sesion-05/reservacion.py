# 1. Leer valor id que representa un número de reservación a imprimir
# 2. Filtrar la lista de reservaciones que coninciden con id
# 3. Imprimir lista de reservaciones

import click
import csv

class Servicio:
    def __init__(self, id_servicio, concepto, cantidad, precio):
        """ Inicializa el objeto Servicio """
        self.id = id_servicio
        self.concepto = concepto
        self.cantidad = cantidad
        self.precio = precio
        
    def __str__(self):
        """ Representación impresa de Servicio """
        return self.concepto
    
    def en_txt(self):
        """ Representación en TXT de un Servicio """
        formato = "{:2} | {:25} | {:3} | {:10.2f}"
        return formato.format(
            self.id, self.concepto, self.cantidad, self.precio)


class Reservacion:
    def __init__(self, lista_servicios):
        """ Constructor del objeto Reservacion """
        self.servicios = lista_servicios


class ReservacionTXT(Reservacion):
    def __init__(self, lista_servicios):
        """ Constructor del objeto ReservacionTXT """
        Reservacion.__init__(self, lista_servicios)
        
    def __str__(self):
        """ Representación en TXT de una Reservación """
        texto = ""
        for servicio in self.servicios:
            texto += servicio.en_txt() + "\n"  # "1  | nom | 1 | .."
        
        return texto

def lee_csv(nomarch):
    """
    Lee los registro de nomarch y regresa como lista de servicios
    """
    with open(nomarch, encoding="utf-8") as da:
        da_csv = csv.reader(da)
        encabezado = next(da_csv)
        # ["ID", "CONCEPTO", "CANTIDAD", "PRECIO"]
        servicios = []
        for fila in da_csv:
            # ["1", "alimentos y bebidas", "1", "1000.00"]
            id_servicio = int(fila[0])
            concepto = fila[1]
            cantidad = int(fila[2])
            precio = float(fila[3])
            
            servicio = Servicio(
                id_servicio, concepto, cantidad, precio)
            
            servicios.append(servicio)
            
    return servicios        

@click.command()
@click.argument("id_servicio", type=int)
def main(id_servicio):
    """ Imprime los servicios de la reservación indicada por ID """
    nomarch = "reservaciones.csv"
    
    lista_de_servicios = lee_csv(nomarch)

    # Filtramos datos
    lista_de_servicios = [
        servicio for servicio in lista_de_servicios
        if servicio.id == id_servicio]
    
    # lista = []
    # for servicio in lista_de_servicios:
    #     if servicio.id == id_servicio:
    #         lista.append(servicio)
    # lista_de_servicios = lista
    
    reservacion_txt = ReservacionTXT(lista_de_servicios)
    print( reservacion_txt )
    

if __name__ == "__main__":
    main()
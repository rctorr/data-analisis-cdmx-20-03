from bottle import route, run
from reservacion import lee_csv, Reservacion


@route("/api/json/<id:int>")
def reservacion(id):
    """ Atiende la petición GET /api/json/<id> """
    nomarch = "reservaciones.csv"

    lista_de_servicios = lee_csv(nomarch)

    # Filtramos datos por id
    lista_de_servicios = [
        servicio for servicio in lista_de_servicios
        if servicio.id == id]
    
    # Creamos un objeto Reservación con la lista de servicios
    reservacion = Reservacion(lista_de_servicios)
    
    respuesta = {
        "id_reservacion" : id,
        "servicios" : reservacion.en_dict()
    }
    
    return respuesta


run(host="127.0.0.1", port=8080, reloader=True)

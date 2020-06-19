from bottle import route, run, template

# GET /hola/rctorr
# POST
# PUT, DELETE, UPDATE
@route("/hola/<nombre>")
def hola(nombre):
    """ Atiende la petición GET /hola/<nombre> """
    return template("<h3>Hola estimad@ {{nom}}</h3>", nom=nombre)

@route("/api/json/usuario")
def json_usuario():
    """ Atiende la petición GET /api/json/usuario """
    usuario = {
        "nombre" : "rctorr",
        "email" : "rictor@cuhrt.com",
        "edad" : 48
    }
    
    return usuario


run(host="127.0.0.1", port=8080)  # 1025->, 8000->
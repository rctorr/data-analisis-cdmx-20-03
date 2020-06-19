from bs4 import BeautifulSoup
import requests

# Obtener el contenido de la página de google.com.mx
# respuesta = requests.get("https://www.google.com.mx/")
respuesta = requests.get("https://unsplash.com/")

# Hay error?
if respuesta.status_code == 200:
    sopa = BeautifulSoup(respuesta.content, features="html.parser")
    print(sopa.title.string)
    imagenes = sopa.find_all("img")
    for imagen in imagenes:
        if "photo" in imagen["src"]:
            print(imagen["src"])
else:
    print("Error al descargar la página")
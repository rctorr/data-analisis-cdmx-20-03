import scrapy

class MercadolibreArania(scrapy.Spider):
    # Nombre de la araña
    name = "mercadolibre"
    # URL del sitio a escarbar
    start_urls = [
        "https://www.mercadolibre.com.mx/ofertas",
    ]
    
    # Que datos y como lo vamos procesar para todos los productos
    def parse(self, respuesta):
        # Lista de todos los productos
        for producto in respuesta.css("div.promotion-item__description"):
            # Filtramos datos para cada una
            yield {
                "nombre" : producto.css("p.promotion-item__title::text").get(),
            }

        # Obtener el elemento que nos lleva a la página siguiente
        pag_sig = respuesta.css("li.andes-pagination__button--next a::attr('href')").get()
        if pag_sig is not None:  # si pag_sig existe!
            yield respuesta.follow(pag_sig, self.parse)
        
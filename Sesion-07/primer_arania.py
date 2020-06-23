import scrapy

class CitasArania(scrapy.Spider):
    # Nombre de la araña
    name = "citas"
    # URL del sitio a escarbar
    start_urls = [
        "http://quotes.toscrape.com/",
    ]
    
    # Que datos y como lo vamos procesar para todas las citas
    def parse(self, respuesta):
        # Lista de todas las citas
        for cita in respuesta.css("div.quote"):
            # Filtramos datos para cada una
            yield {
                "texto" : cita.css("span.text::text").get(),
                "autor" : cita.xpath("span/small/text()").get(),
            }

        # Obtener el elemento que nos lleva a la página siguiente
        pag_sig = respuesta.css("li.next a::attr('href')").get()
        if pag_sig is not None:  # si pag_sig existe!
            yield respuesta.follow(pag_sig, self.parse)
        
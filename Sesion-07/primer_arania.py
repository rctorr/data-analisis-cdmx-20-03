import scrapy

class CitasArania(scrapy.Spider):
    # Nombre de la araña
    name = "citas"
    # URL del sitio a escarbar
    start_urls = [
        "http://quotes.toscrape.com/",
    ]
    
    # Que datos y como lo vamos procesar
    def parse(self, respuesta):
        # Lista de todas las citas
        for cita in respuesta.css("div.quote"):
            yield {
                "texto" : cita.css("span.text::text").get(),
                "autor" : cita.xpath("span/small/text()").get(),
            }

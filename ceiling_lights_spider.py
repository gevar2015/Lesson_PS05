import scrapy

class CeilingLightsSpider(scrapy.Spider):
    name = 'ceiling_lights'
    allowed_domains = ['divan.ru']
    start_urls = ['https://divan.ru/category/potolocnye-svetilniki']

    def parse(self, response):
        # Находим товары на странице
        products = response.css('div._Ud0k')
        for product in products:
            yield {
                "name": product.css('div.lsooF span::text').get(),
                "price": product.css('div.pY3d2 span::text').get(),
                "url": product.css('a').attrib['href']
            }

import scrapy

class CeilingLightsSpider(scrapy.Spider):
    name = 'ceiling_lights'
    allowed_domains = ['divan.ru']
    start_urls = ['https://www.divan.ru/category/potolocnye-svetilniki']

    def parse(self, response):
        # Находим первый товар на странице
        product = response.css('div.product-card__info').get()

        if product:
            title = response.css('div.product-card__title::text').get()
            price = response.css('div.product-price__current::text').get()
            link = response.css('a.product-card__link::attr(href)').get()

            # Выводим данные в терминал
            print(f"Название: {title.strip() if title else 'N/A'}")
            print(f"Цена: {price.strip() if price else 'N/A'}")
            print(f"Ссылка: {response.urljoin(link) if link else 'N/A'}")

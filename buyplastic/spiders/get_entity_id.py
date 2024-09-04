import scrapy
from scrapy.cmdline import execute
from scrapy.exceptions import CloseSpider
from buyplastic.items import getEntityItem


class GetEntityIdSpider(scrapy.Spider):
    name = "get_entity_id"
    def start_requests(self):
        for page in range(1,10):
            url = f"https://buyplastic.com/categories/?page={page}"
            yield scrapy.Request(url=url, callback=self.get_product_link)
    def get_product_link(self, response):
        item = getEntityItem()

        if "404 Error" in response.text:
            raise CloseSpider("Page not found")

        products = response.xpath("//ul[@class='productGrid']//li[@class='product']")
        for product in products:
            product_link = product.xpath(".//h3/a/@href").get()
            status = 0

            item['product_link'] = product_link
            item['status'] = status

            yield item

if __name__ == "__main__":
    execute("scrapy crawl get_entity_id".split())


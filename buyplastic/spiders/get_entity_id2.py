import scrapy
from scrapy.cmdline import execute
from buyplastic.db_config import DbConfig
import regex as re
from scrapy.exceptions import CloseSpider
from buyplastic.items import getEntityItem2

obj_db = DbConfig()

class GetEntityId2Spider(scrapy.Spider):
    name = "get_entity_id2"

    def start_requests(self):
        results = obj_db.collection_link.find({'status':0})
        for result in results:
            product_link = result['product_link']
            metadict = dict()
            metadict['product_link'] = product_link
            yield scrapy.Request(product_link, callback=self.parse, meta=metadict)

    def parse(self, response):
        item = getEntityItem2()
        if response.status != 200:
            raise CloseSpider("Response error")
        entity_id_ = re.findall('ProductID.*?,',response.text)[0]
        entity_id = entity_id_.replace('ProductID: "','').replace('"','').replace(',','')
        item['product_link'] = response.meta['product_link']
        item['entity_id'] = entity_id
        item['status'] = 0
        yield item

if __name__=="__main__":
    execute("scrapy crawl get_entity_id2".split())

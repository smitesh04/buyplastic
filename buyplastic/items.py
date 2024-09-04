# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BuyplasticItem(scrapy.Item):
    # define the fields for your item here like:
    product_link = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    pass

class getEntityItem(scrapy.Item):
    product_link = scrapy.Field()
    status = scrapy.Field()

class getEntityItem2(scrapy.Item):
    product_link = scrapy.Field()
    entity_id = scrapy.Field()
    status = scrapy.Field()

class addVariants(scrapy.Item):
    product_link = scrapy.Field()
    entity_id = scrapy.Field()
    variant_combinations = scrapy.Field()
    all_variants_with_name = scrapy.Field()
    product_title = scrapy.Field()
    status = scrapy.Field()

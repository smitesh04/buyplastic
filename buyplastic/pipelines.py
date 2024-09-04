# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from buyplastic.db_config import DbConfig
from buyplastic.items import getEntityItem, getEntityItem2, addVariants, BuyplasticItem
obj_db = DbConfig()

class BuyplasticPipeline:

    def process_item(self, item, spider):
        if isinstance(item, getEntityItem):
            try:obj_db.collection_link.insert_one(dict(item))
            except Exception as e:
                print(f"Failed to insert item to DB: {str(e)}")

        if isinstance(item, getEntityItem2):
            try:
                obj_db.collection_entity.insert_one(dict(item))
                myquery = {"product_link": item["product_link"]}
                newvalues = {"$set": {"status": "1"}}
                obj_db.collection_link.update_one(myquery, newvalues)
            except Exception as e:
                print(f"Failed to insert item to DB: {str(e)}")

        if isinstance(item, addVariants):
            try:obj_db.collection_variants.insert_one(dict(item))
            except Exception as e:
                print(f"Failed to insert item to DB: {str(e)}")

        if isinstance(item, BuyplasticItem):
            try:
                obj_db.collection_data.insert_one(dict(item))
                myquery = {"product_link": item["product_link"]}
                newvalues = {"$set": {"status": "1"}}
                obj_db.collection_variants.update_one(myquery, newvalues)
            except Exception as e:
                print(f"Failed to insert item to DB: {str(e)}")

        return item

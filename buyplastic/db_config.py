import pymongo

class DbConfig():
    con = pymongo.MongoClient(host="mongodb://localhost:27017/")
    db = con["buyplastic"]
    collection_link = db["product_links"]
    collection_link.create_index("product_link", unique=True)

    collection_entity = db['entity_ids']
    collection_entity.create_index("entity_id", unique=True)

    collection_variants = db['variants']
    collection_variants.create_index("product_link", unique=True)

    collection_data = db['data']





import scrapy
from buyplastic.db_config import DbConfig
from scrapy.exceptions import CloseSpider
from scrapy.cmdline import execute
import pandas as pd
from buyplastic.items import addVariants

obj_db = DbConfig()


class AddVariantsSpider(scrapy.Spider):
    name = "add_variants"

    def start_requests(self):
        results = obj_db.collection_entity.find({'status':0})
        for result in results:
            product_link = result['product_link']
            metadict = dict()
            metadict['product_link'] = product_link
            metadict['entity_id'] = result['entity_id']
            yield scrapy.Request(url=product_link, callback=self.parse, meta=metadict)

    def parse(self, response):
        item = addVariants()
        if response.status != 200:
            raise CloseSpider("response status: %d" % response.status)

        product_title = response.xpath("//h1[contains(@class,'productView-title')]/text()").get()
        form_radio_path = response.xpath('//input[@class="form-radio"]')

        all_variants_dict = dict()
        variant_name_list = []
        variant_value_list = []

        for form_radio in form_radio_path:
            variant_name = form_radio.xpath('./@name').get()
            variant_name_list.append(variant_name)
            variant_value = form_radio.xpath('./@value').get()
            all_variants_dict_value = response.xpath(f'//label[contains(@data-product-attribute-value,{variant_value})]/span/text()').get()
            if all_variants_dict_value is None:
                all_variants_dict_value = response.xpath(f'//label[contains(@data-product-attribute-value,{variant_value})]/span/@title').get()
                print()
            all_variants_dict_value = all_variants_dict_value.replace('\r\n', '').strip()
            if all_variants_dict_value == '':
                all_variants_dict_value = response.xpath(f'//label[contains(@data-product-attribute-value,{variant_value})]/span/@title').get()
                print()
            all_variants_dict[variant_value] = all_variants_dict_value
            variant_value_list.append(variant_value)

        variant_name_form = response.xpath("//div[@data-product-attribute='set-select']/select[contains(@class,'form-select')]/@name").get()
        for form_select in response.xpath("//div[@data-product-attribute='set-select']/select[contains(@class,'form-select')]/option"):

            variant_value_form = form_select.xpath('.//@data-product-attribute-value').get()
            if variant_value_form != None:
                variant_value_list.append(variant_value_form)
                variant_name_list.append(variant_name_form)
                all_variants_dict_value = form_select.xpath('./text()').get()
                try:all_variants_dict_value = all_variants_dict_value.replace('\r\n', '').strip()
                except:all_variants_dict_value = ''
                all_variants_dict[variant_value_form] = all_variants_dict_value
                print()

        variant_dict = {'variant_name': variant_name_list, 'variant_value': variant_value_list}
        df = pd.DataFrame(variant_dict)
        variant_name_unique = df['variant_name'].unique().tolist()
        variant_combinations = {}

        for v in variant_name_unique:
            variant_values_df = df[df['variant_name'].isin([v])]['variant_value'].tolist()
            variant_combinations[v] = variant_values_df

        item['variant_combinations'] = variant_combinations
        item['product_title'] = product_title
        item['all_variants_with_name'] = all_variants_dict
        item['entity_id'] = response.meta['entity_id']
        item['product_link'] = response.meta['product_link']
        item['status'] = 0

        yield item

if __name__ == '__main__':
    execute("scrapy crawl add_variants".split())









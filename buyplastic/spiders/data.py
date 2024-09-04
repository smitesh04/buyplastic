import scrapy
from scrapy.cmdline import execute
from scrapy.exceptions import CloseSpider
from buyplastic.db_config import DbConfig
import itertools
import json
import urllib
from buyplastic.items import BuyplasticItem

obj_db = DbConfig()

class DataSpider(scrapy.Spider):
    name = "data"
    handle_httpstatus_list = [403]

    def start_requests(self):
        results = obj_db.collection_variants.find({'status':0})
        for result in results:
            all_variants_with_name = result['all_variants_with_name']
            product_link = result['product_link']
            entity_id = result['entity_id']
            variant_combinations = result['variant_combinations']

            values_lists = variant_combinations.values()
            combinations = list(itertools.product(*values_lists))
            combinations_dicts = [
                dict(zip(variant_combinations.keys(), combination))
                for combination in combinations
            ]
            for combo in combinations_dicts:
                print(combo)

                payload_dict = {}
                for key,value in combo.items():
                    payload_dict[key] = str(value)
                payload_dict['action'] = 'add'
                payload_dict['product_id'] = str(entity_id)
                payload_dict['qty[]'] = '1'


                url = f"https://buyplastic.com/remote/v1/product-attributes/{entity_id}"
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'cookie': '__cf_bm=JXK5fYbCbNgPn.EjvUxLy9sH7nOAKB25kpyXfgIW0ec-1725276210-1.0.1.1-foCx6HqSNfoA3J1tBApuLNUuXN1lU_Suqge9cbFd3uzDOOAa9y2ZV6sZ4tQA0Q7IMocyhPU.9t0BD8Sq6PQpOw; fornax_anonymousId=8c061720-96b3-4f81-a035-1806e7ffa5a3; athena_short_visit_id=450a51c2-dc51-40cc-8a08-f046fd0cdb22:1725276274; SF-CSRF-TOKEN=271afa93-63b8-443b-9fa1-9a646ce25ca9; XSRF-TOKEN=e762dc6bbe31b7b5bf2524d4ab3e6244805eeb5d3fb1d80ba959f9e1ad2d620c; SHOP_SESSION_TOKEN=4792fdbf-c6e0-4146-81f5-20b30d32b596; _gid=GA1.2.1534358867.1725276275; _gat=1; _fbp=fb.1.1725276275472.49986302738933925; STORE_VISITOR=1; _ga=GA1.1.1664259461.1725276275; _gcl_au=1.1.555946359.1725276276; _uetsid=ef138270691d11efb1656be526393822; _uetvid=ef13d190691d11ef81ebadd947d1c5c8; _clck=imkmkp%7C2%7Cfou%7C0%7C1706; _clsk=7oe8hb%7C1725276277841%7C5%7C1%7Cx.clarity.ms%2Fcollect; _ga_YBZ6F6339N=GS1.1.1725274357.10.1.1725276290.0.0.0; _ga_50BLGJTDSB=GS1.1.1725274357.9.1.1725276290.44.0.0; Shopper-Pref=5EABF5E6BAECE1A3BB15A0003EE82CC2C4FEB1DE-1725881094948-x%7B%22cur%22%3A%22USD%22%7D; SF-CSRF-TOKEN=6b1afe56-133f-4e5e-b80e-2098cd702806; SHOP_SESSION_TOKEN=4792fdbf-c6e0-4146-81f5-20b30d32b596; Shopper-Pref=32809BE4C551EE8053EA23AA8BD5F935C04C9547-1725881490228-x%7B%22cur%22%3A%22USD%22%7D; XSRF-TOKEN=e762dc6bbe31b7b5bf2524d4ab3e6244805eeb5d3fb1d80ba959f9e1ad2d620c; __cf_bm=Cjd8cGMNdfoIPVjgKSIM_DQQQtuJIcHTX4mYabtaz1U-1725276479-1.0.1.1-ai2br7nzKPvdWCQNMx0wjc6W9XdB2BAkBlBIP1bxOi1pSsAVF3UXHTNg0B9LRBsgcvs6MbtROOMbPGaqzsIJrA; athena_short_visit_id=450a51c2-dc51-40cc-8a08-f046fd0cdb22:1725276274; fornax_anonymousId=8c061720-96b3-4f81-a035-1806e7ffa5a3',
                    'origin': 'https://buyplastic.com',
                    'priority': 'u=1, i',
                    'referer': 'https://buyplastic.com/products/multiwall-polycarbonate-sheet.html',
                    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'stencil-config': '{}',
                    'stencil-options': '{"render_with":"products/bulk-discount-rates"}',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
                    'x-requested-with': 'stencil-utils',
                    'x-sf-csrf-token': '271afa93-63b8-443b-9fa1-9a646ce25ca9',
                    'x-xsrf-token': 'e762dc6bbe31b7b5bf2524d4ab3e6244805eeb5d3fb1d80ba959f9e1ad2d620c'
                }

                metadict = {}
                metadict['product_link'] = product_link
                metadict['entity_id'] = entity_id
                metadict['headers'] = headers
                metadict['payload_dict'] = payload_dict
                metadict['all_variants_with_name'] = all_variants_with_name
                metadict['product_title'] = result['product_title']

                # yield scrapy.Request(method='POST', url=url, headers=headers, body=json.dumps(payload_dict), callback=self.parse, meta = metadict)
                yield scrapy.FormRequest(method='POST', url=url, headers=headers, formdata=payload_dict, callback=self.parse, meta = metadict)


    def parse(self, response):

        if response.status == 200:
            all_variants_with_name = response.meta['all_variants_with_name']
            payload_dict = response.meta['payload_dict']
            product_title = response.meta['product_title']
            product_title_tail = list()
            for k,v in payload_dict.items():
                if 'attribute' in k:
                    variant = all_variants_with_name[v]
                    product_title_tail.append(variant)
            product_title_final = product_title +' - '+' - '.join(product_title_tail)

            jsn = json.loads(response.text)

            try:price = jsn['data']['price']['without_tax']['value']
            except:price = ''

            item = BuyplasticItem()
            item['product_link'] = response.meta['product_link']
            item['product_name'] = product_title_final
            item['product_price'] = price

            yield item

if __name__ == "__main__":
    execute("scrapy crawl data".split())
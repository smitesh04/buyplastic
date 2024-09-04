import requests

cookies = {
    '__cf_bm': 'JXK5fYbCbNgPn.EjvUxLy9sH7nOAKB25kpyXfgIW0ec-1725276210-1.0.1.1-foCx6HqSNfoA3J1tBApuLNUuXN1lU_Suqge9cbFd3uzDOOAa9y2ZV6sZ4tQA0Q7IMocyhPU.9t0BD8Sq6PQpOw',
    'fornax_anonymousId': '8c061720-96b3-4f81-a035-1806e7ffa5a3',
    'athena_short_visit_id': '450a51c2-dc51-40cc-8a08-f046fd0cdb22:1725276274',
    'SF-CSRF-TOKEN': '271afa93-63b8-443b-9fa1-9a646ce25ca9',
    'XSRF-TOKEN': 'e762dc6bbe31b7b5bf2524d4ab3e6244805eeb5d3fb1d80ba959f9e1ad2d620c',
    'SHOP_SESSION_TOKEN': '4792fdbf-c6e0-4146-81f5-20b30d32b596',
    '_gid': 'GA1.2.1534358867.1725276275',
    '_gat': '1',
    '_fbp': 'fb.1.1725276275472.49986302738933925',
    'STORE_VISITOR': '1',
    '_ga': 'GA1.1.1664259461.1725276275',
    '_gcl_au': '1.1.555946359.1725276276',
    '_uetsid': 'ef138270691d11efb1656be526393822',
    '_uetvid': 'ef13d190691d11ef81ebadd947d1c5c8',
    '_clck': 'imkmkp%7C2%7Cfou%7C0%7C1706',
    '_clsk': '7oe8hb%7C1725276277841%7C5%7C1%7Cx.clarity.ms%2Fcollect',
    '_ga_YBZ6F6339N': 'GS1.1.1725274357.10.1.1725276290.0.0.0',
    '_ga_50BLGJTDSB': 'GS1.1.1725274357.9.1.1725276290.44.0.0',
    'Shopper-Pref': '5EABF5E6BAECE1A3BB15A0003EE82CC2C4FEB1DE-1725881094948-x%7B%22cur%22%3A%22USD%22%7D',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__cf_bm=JXK5fYbCbNgPn.EjvUxLy9sH7nOAKB25kpyXfgIW0ec-1725276210-1.0.1.1-foCx6HqSNfoA3J1tBApuLNUuXN1lU_Suqge9cbFd3uzDOOAa9y2ZV6sZ4tQA0Q7IMocyhPU.9t0BD8Sq6PQpOw; fornax_anonymousId=8c061720-96b3-4f81-a035-1806e7ffa5a3; athena_short_visit_id=450a51c2-dc51-40cc-8a08-f046fd0cdb22:1725276274; SF-CSRF-TOKEN=271afa93-63b8-443b-9fa1-9a646ce25ca9; XSRF-TOKEN=e762dc6bbe31b7b5bf2524d4ab3e6244805eeb5d3fb1d80ba959f9e1ad2d620c; SHOP_SESSION_TOKEN=4792fdbf-c6e0-4146-81f5-20b30d32b596; _gid=GA1.2.1534358867.1725276275; _gat=1; _fbp=fb.1.1725276275472.49986302738933925; STORE_VISITOR=1; _ga=GA1.1.1664259461.1725276275; _gcl_au=1.1.555946359.1725276276; _uetsid=ef138270691d11efb1656be526393822; _uetvid=ef13d190691d11ef81ebadd947d1c5c8; _clck=imkmkp%7C2%7Cfou%7C0%7C1706; _clsk=7oe8hb%7C1725276277841%7C5%7C1%7Cx.clarity.ms%2Fcollect; _ga_YBZ6F6339N=GS1.1.1725274357.10.1.1725276290.0.0.0; _ga_50BLGJTDSB=GS1.1.1725274357.9.1.1725276290.44.0.0; Shopper-Pref=5EABF5E6BAECE1A3BB15A0003EE82CC2C4FEB1DE-1725881094948-x%7B%22cur%22%3A%22USD%22%7D',
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
    'x-xsrf-token': 'e762dc6bbe31b7b5bf2524d4ab3e6244805eeb5d3fb1d80ba959f9e1ad2d620c',
}

data = {
    'action': 'add',
    'attribute[620]': '2491',
    'attribute[621]': '2493',
    'attribute[622]': '2498',
    'attribute[623]': '2500',
    'product_id': '1826',
    'qty[]': '1',
}

response = requests.post('https://buyplastic.com/remote/v1/product-attributes/1826', cookies=cookies, headers=headers, data=data)
print(response.text)
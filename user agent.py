import requests
from parsel import Selector
url='http://www.porters.vip/verify/uas/index.html'


# headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
headers = {'User-Agent': 'PostmanRuntime/7.26.2',
           'Host': 'www.porters.vip',
           'Accept':'*/*',
           'Connection':'keep-alive',
           'Accept-Endcoding':'gzip,deflate,br'}
r=requests.get(url,headers=headers)
sel = Selector(r.text)
print(r.status_code)
print(sel.css('.list-group-item::text').extract())



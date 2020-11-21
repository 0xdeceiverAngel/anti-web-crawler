import requests
import re
from parsel import Selector

url = 'http://www.porters.vip/confusion/flight.html'
resp = requests.get(url)
sel = Selector(resp.text)
em = sel.css('em.rel').extract()


for element in em:
    element = Selector(element)
    element_b = element.css('b').extract()
    b_f = Selector(element_b.pop(0)) #base price
    base_price = b_f.css('i::text').extract()
    # print(b_f.css('i::attr("style")').extract())
    base_offset = int(
        ''.join(re.findall('width:(.*)px', b_f.css('i::attr("style")').extract().pop(0))))

    alternate_price = []
    for eb in element_b: # offset left

        ss = len(element_b)
        eb = Selector(eb)
        style = eb.css('b::attr("style")').get()
        position = ''.join(re.findall('left:(.*)px', style))
        value = eb.css('b::text').get()
        alternate_price.append({'position': position, 'value': value})

        for al in alternate_price:
            position = int(al.get('position'))
            value = al.get('value')
            index = int(position / base_offset)
            base_price[index] = value
    print(base_price)

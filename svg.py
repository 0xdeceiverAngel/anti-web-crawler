import requests
import re
from parsel import Selector

url_css = 'http://www.porters.vip/confusion/css/food.css'
url_svg = 'http://www.porters.vip/confusion/font/food.svg'
css_class_prefix = 'vhk'

css_resp = requests.get(url_css).text
svg_resp = requests.get(url_svg).text
css_resp=css_resp.replace(' ', '')
# print(css_resp,'','')
class_found = re.findall('\.vhk.*{\nbackground:-(\d+)px-(\d+)px;', css_resp)


svg_data = Selector(svg_resp)
texts = svg_data.xpath('//text')



# print(class_found)
for i in class_found:
    x ,y = i[0] ,i[1]
    # print(x,y)
    axis_y = [i.attrib.get('y')
              for i in texts if int(y) <= int(i.attrib.get('y'))][0]
    svg_text = svg_data.xpath('//text[@y="%s"]/text()' % axis_y).extract_first()
    font_size = re.search('font-size:(\d+)px', svg_resp).group(1)
    position = int(x) // int(font_size)
    number = svg_text[position]
    print(number)







import requests
from random import *
from parsel import Selector
import hashlib
from time import time

# headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
headers = {'User-Agent': 'PostmanRuntime/7.26.2',
           'Host': 'www.porters.vip',
           'Accept':'*/*',
           'Connection':'keep-alive',
           'Accept-Endcoding':'gzip,deflate,br'}
act = "".join([str(randint(1, 9)) for i in range(5)])
tim=round(time())
rand = "".join(sample([chr(i) for i in range(65, 91)], 5))
val=act+str(tim)+rand

manip = hashlib.md5()
manip.update(val.encode('utf-8'))
sign = manip.hexdigest()
url =f'http://www.porters.vip/verify/sign/fet?actions={act}&tim={tim}&randstr={rand}&sign={sign}'
print(url+'\n',tim,act,rand,sign)
r=requests.get(url,headers=headers)
print(r.status_code)
print(r.content)


from selenium.webdriver import Chrome
import time
from selenium.webdriver import ChromeOptions
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# browser = Chrome(options=option)
browser = Chrome()
browser.get('http://www.porters.vip/features/webdriver.html')
script = 'Object.defineProperty(navigator, "webdriver", {get: () => false,});'
browser.execute_script(script)
time.sleep(2)
browser.find_element_by_css_selector('.btn.btn-primary.btn-lg').click()
elements = browser.find_element_by_css_selector('#content')
time.sleep(2)
print(elements.text)
# browser.close()
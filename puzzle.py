from selenium import webdriver


browser = webdriver.Chrome()
browser.get('http://www.porters.vip/captcha/jigsawCanvas.html')

jigsawCircle = browser.find_element_by_css_selector('#jigsawCircle')
jigsawCanvas = browser.find_element_by_css_selector('#jigsawCanvas')
jigsawCanvas.screenshot('before.png')
action = webdriver.ActionChains(browser)
action.click_and_hold(jigsawCircle).perform()
scripts = """
var missblock = document.getElementById('missblock');
missblock.style['visibility'] = 'hidden';
"""
browser.execute_script(scripts)
jigsawCanvas.screenshot('after.png')

from PIL import Image
image_a = Image.open('after.png')
image_b = Image.open('before.png')

from PIL import ImageChops
diff = ImageChops.difference(image_b, image_a)
diff_position = diff.getbbox()
print(diff_position)

position_x = diff_position[0]
action.move_by_offset(int(position_x)-10, 0)
action.release().perform()
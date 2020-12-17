from selenium import webdriver


browser = webdriver.Chrome()
browser.get('http://www.porters.vip/captcha/sliders.html')
hover = browser.find_element_by_css_selector('.hover')

action = webdriver.ActionChains(browser)
action.click_and_hold(hover).perform()  
action.move_by_offset(340, 0)  
action.release().perform() 
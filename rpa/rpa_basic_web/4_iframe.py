import time
from selenium import webdriver


browser = webdriver.Chrome("./chromedriver")
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')


# 요소에 해당하는 아이프레임으로 프레임 이동 후 과정 수행 후 아이프레임 다시 빠져나옴
browser.switch_to.frame('iframeResult')
elem = browser.find_element_by_xpath('//*[@id="css"]')
elem.click()
browser.switch_to.default_content()





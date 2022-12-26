import time
from selenium import webdriver

# 체크 박스 = 여러개 선택가능함(라디오 버튼과 차이)

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult')

elem1 = browser.find_element_by_xpath('//*[@id="vehicle1"]')

if elem1.is_selected() == False:
    print("선택되어있지 않아서 선택함")
    elem1.click()
else: # 라디오 버튼이 선택되어있음
    print("암것도 안함")

elem2 = browser.find_element_by_xpath('//*[@id="vehicle2"]')

if elem2.is_selected() == False:
    print("선택되어있지 않아서 선택함")
    elem2.click()
else: # 라디오 버튼이 선택되어있음
    print("암것도 안함")

elem3 = browser.find_element_by_xpath('//*[@id="vehicle3"]')

if elem3.is_selected() == False:
    print("선택되어있지 않아서 선택함")
    elem3.click()
else: # 라디오 버튼이 선택되어있음
    print("암것도 안함")




browser.switch_to.default_content()

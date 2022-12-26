import time
from selenium import webdriver

# 라디오 버튼 = 체크박스인데 한가지만 선택가능

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')
elem = browser.find_element_by_xpath('//*[@id="css"]')

# 해당 선택이 체크 안되어있으면 체크하기
if elem.is_selected() == False:
    print("선택되어있지 않아서 선택함")
    elem.click()
else: # 라디오 버튼이 선택되어있음
    print("암것도 안함")

time.sleep(5)

if elem.is_selected() == False:
    print("선택되어있지 않아서 선택함")
    elem.click()
else: # 라디오 버튼이 선택되어있음
    print("암것도 안함")


browser.switch_to.default_content()

browser.quit()


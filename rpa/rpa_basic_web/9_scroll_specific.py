from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화
browser.get('https://www.w3schools.com/html/default.asp')

time.sleep(5)

# 특정영역 스크롤
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')
# elem.click()

# 방법 1 : ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()
# elem.click()


# 방법 2 : 좌표 정보 이용
# xy = elem.location_once_scrolled_into_view # 함수가 아닌 변수임
# elem.click()

time.sleep(5)

browser.quit()
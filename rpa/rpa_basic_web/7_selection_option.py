from selenium import webdriver
import time


browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# 옵션으로 선택
elem1 = browser.find_element_by_xpath('//*[@id="cars"]/option[1]')
elem1.click() # cars 안에 첫번째 옵션 클릭

time.sleep(3)

# 완벽히 텍스트와 일치
elem1 = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
elem1.click() # cars 안에 아우디 옵션 클릭

time.sleep(3)

# 특정 부분만 일치
elem1 = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Op")]')
elem1.click() # cars 안에 Op 포함한 옵션 클릭



browser.switch_to.default_content()

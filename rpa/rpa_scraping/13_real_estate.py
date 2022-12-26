from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup




browser = webdriver.Chrome("./personal_thing/chromedriver")
browser.maximize_window() # 창 최대화
browser.get('https://land.naver.com/')

elem = browser.find_element_by_id("queryInputHeader")
elem.send_keys("성환 e편한세상")
elem.send_keys(Keys.ENTER)

time.sleep(1)


soup = BeautifulSoup(browser.page_source, "lxml")
houses = soup.find_all("a", attrs={"class" : "item_link"})

for house in houses:
    name = house.find("span", attrs={"class" : "text"}).get_text()
    type = house.find("span", attrs={"class" : "type"}).get_text()
    price = house.find("span", attrs={"class" : "price"}).get_text()
    spec = house.find("span", attrs={"class" : "spec"}).get_text()

    print(name)
    print(type)
    print(price)
    print(spec)
    print("-"*100)



browser.quit()
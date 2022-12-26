

# https://www.w3schools.com/
# //*[@id="main"]/div[1]/div/div[1]/a[1] #learn html click
# //*[@id="topnav"]/div/div/a[10] # how to click
# //*[@id="leftmenuinnerinner"]/a[116] # contact form

# first_name = "목" //*[@id="fname"]
# last_name = "'재민" //*[@id="lname"]
# country = "Canada" 
# elem1 = browser.find_element_by_xpath('//*[@id="country"]/option[text()="Canada"]')
# subject = "퀴즈 완료했습니다." //*[@id="main"]/div[3]/textarea

# //*[@id="main"]/div[3]/a

from selenium import webdriver
import time

first_name = "목"
last_name = "재민" 
country = "Canada" 
subject = "퀴즈 완료했습니다."

browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()
browser.get('https://www.w3schools.com/')

browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()

elem1 = browser.find_element_by_xpath('//*[@id="fname"]')
elem1.send_keys(first_name)

elem2 = browser.find_element_by_xpath('//*[@id="lname"]')
elem2.send_keys(last_name)

elem3 = browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country))
elem3.click()

elem4 = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
elem4.send_keys(subject)

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

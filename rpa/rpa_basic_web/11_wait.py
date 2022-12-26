from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome('./chromedriver')
browser.get('https://beta-flight.naver.com/')
browser.maximize_window()

# 해당 엑스패스를 찾을 때까지 기다린 후 실행
try:
    element = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located(By.XPATH, '//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/button'))
except:
    print("실패")

# 해당 요소에 값 출력
# print(elem.text)




time.sleep(3)
browser.quit()


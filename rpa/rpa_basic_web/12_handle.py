from selenium import webdriver
import time
# 창전환


browser = webdriver.Chrome('./chromedriver')
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')

curr_handle = browser.current_window_handle
print(curr_handle) # 현재 윈도우 핸들정보

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle)  # 각 핸들 정보
    browser.switch_to_window(handle) # 각 핸들로 이동
    print(browser.title) # 현재 핸들의 제목 표시
    print() # 줄 바꿈

print("현재 핸들 닫기")
browser.close()
print("처음 핸들")
browser.switch_to_window(curr_handle)

print(browser.title)


time.sleep(3)
browser.get('http://daum.net')

time.sleep(3)
browser.quit()

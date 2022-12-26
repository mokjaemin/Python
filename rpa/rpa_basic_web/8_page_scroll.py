from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() # 창 최대화
browser.get('https://shopping.naver.com/home/p/index.nhn')

# # 무선 마우스 입력 후 검색 버튼 클릭
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys("무선마우스")
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 무선 마우스 입력 후 엔터
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys("무선마우스")
elem.send_keys(Keys.ENTER)


# 스크롤
# 지정한 위치로 스크롤 내리기
# browser.execute_script('window.scrollTo(0,1600)') # 1600 만큼 내리기

# 해당 화면 가장 아래로 내리기
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') # 화면 기준 끝까지 내림


# 동적페이지에 대해서 마지막까지 스크롤 내림
interval = 2 # 2초에 한번씩 내림

# 현재 문서의 높이를 가져와 저장
prev_height = browser.execute_script('return document.body.scrollHeight')


# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    
    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    current_height = browser.execute_script('return document.body.scrollHeight')

    if current_height == prev_height:
        print("탈출")
        break # 높이 변화가 없으면 반복문 탈출
    
    prev_height = current_height


# 맨위로 올리기
browser.execute_script('window.scrollTo(0,0)')
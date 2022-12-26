import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
import time


for i in range(1, 2):

    url = "https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EA%B1%B4%EC%A1%B0%EA%B8%B0&pagingIndex=2&pagingSize=40&productSet=total&query=%EA%B1%B4%EC%A1%B0%EA%B8%B0&sort=rel&timestamp=&viewType=list".format(i)
    
    browser = webdriver.Chrome('./personal_thing/chromedriver')
    browser.maximize_window() # 창 최대화
    browser.get(url)


    # 동적페이지에 대해서 마지막까지 스크롤 내림
    interval = 1 # 2초에 한번씩 내림

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
            break # 높이 변화가 없으면 반복문 탈출
        
        prev_height = current_height



    # headers = {"user-gent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    # res = requests.get(url)
    # res.raise_for_status()

    soup = BeautifulSoup(browser.page_source, "lxml")



    items = soup.find_all("li", attrs={"class" : re.compile("^basicList_item")})
    for item in items:

        # 광고 제품 제외
        # ad_badge = item.find("button", attrs={"class" : re.compile("^ad_ad")})
        # if ad_badge:
        #     # print("광고 상품 제외")
        #     continue

        titles = item.find("a", attrs={"class" : re.compile("^basicList_link")}).get_text()
        prices = item.find("span", attrs={"class" : re.compile("^price_num")}).get_text()
        prices = prices[0:-1] # 맨끝에 '원' 제외
        prices = int(prices.replace(',','')) # 콤마제외
        links = item.a["href"]
        usage = item.find("a", attrs={"class" : re.compile("27Krk$")})

        if usage:
            usage1 = usage.get_text()
        else:
            usage1 = "없음"


        if "삼성" in titles:
            print(f"제품명 : {titles}")
            print(f"가격 : {prices}")
            print(f"{usage1}")
            print(f"링크 : {links}")
            print("-"*100)



        # 특정 이름이 들어간 제품 제외
        if "Apple" in titles:
            continue
            
        
        
        # 검색 조건 걸기
        # if int(prices) > int(1000000):
        #     print(titles + " : " + str(prices) + "원")


        # print(f"제품명 : {titles}")
        # print(f"가격 : {prices}")
        # print(f"링크 : {links}")
        # print("-"*100)


    

    

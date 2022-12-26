import requests
from bs4 import BeautifulSoup
from requests.api import head
from selenium import webdriver
import time


# 크롬을 백그라운드에서 실행
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")



url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Accept-Language" : "ko-KR, ko"
    }
# 구글 무비가 나라마다 화면이 달라서 한국으로 설정해서 접근


browser = webdriver.Chrome('./personal_thing/chromedriver', options=options)
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


browser.get_screenshot_as_file("google_movie.png")




soup = BeautifulSoup(browser.page_source, "lxml")


# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class" : "Vpfmgd"})
# 내려갈떄 class 명이 달라질 수 있음을 주의하자

# print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify()) # html 문서를 정돈해서 출력

for movie in movies:
    title = movie.find("div", attrs={"class" : "WsMG1c nnK0zc"}).get_text()
    price = movie.find("span", attrs={"class" : "VfPpfd ZdBevf i5DZme"}).get_text()
    link = movie.a["href"]
    print(title)
    print(price)
    print("http://play.google.com" + link)
    print("-"*100)

browser.quit()
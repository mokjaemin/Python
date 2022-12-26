
# user agent 는 request 정보가 200이 아닐 시 접근 권한 부여를 위한 툴
# 하지만 잘 안되어서 뷰티풀수프로 하는게 나음

import requests
from bs4 import BeautifulSoup


# url = "http://nadocoing.tistory.com"
# headers = {"user-gent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
# # google에 user agent string을 통해 알 수 있음

# res = requests.get(url, headers=headers)
# res.raise_for_status()


# with open("nadocoding.html", "w", encoding="utf8") as f:
#     f.write(res.text)

url = "https://nadocoding.tistory.com"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)
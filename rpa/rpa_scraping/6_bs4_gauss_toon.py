import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# link = cartoons[0].a["href"]


# command + click -> 바로 링크로 이동 가능
# print("https://comic.naver.com" + link)


# 웹툰 제목 및 링크 출력
cartoons = soup.find_all("td", attrs={"class" : "title"})
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title, link)



# # 웹툰 평점 구하기
# total_rates = 0
# ratings = soup.find_all("div", attrs={"class" : "rating_type"})
# for rating in ratings:
#     rate = rating.strong.get_text()
#     print(rate)
#     total_rates += float(rate)

# print("전체 평점 : " + str(total_rates))
# print("평균 평점 : " + str((total_rates / len(ratings))))




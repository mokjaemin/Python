import requests
from bs4 import BeautifulSoup


# 2015부터 2020까지 영화 순위

for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    imgaes = soup.find_all("img", attrs={"class" : "thumb_img"})

    for idx, image in enumerate(imgaes): # enumerate - 크기 측정
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "http:" + image_url

        print(image_url)
        image_res =requests.get(image_url)
        image_res.raise_for_status()
            

        with open("movie{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)

        if idx >= 4:
            break # 상위 5개만 다운로드
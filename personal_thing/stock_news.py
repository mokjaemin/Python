import requests
from bs4 import BeautifulSoup
import csv

# 네이버 주식 뉴스



url = "https://finance.naver.com/news/news_list.nhn?mode=RANK&page="
filename = "주식_탑뉴스.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") 
writer = csv.writer(f)
# split('\t') 빈공간으로 항목 구별 res->[N, 종목명, ...]

for page in range(0,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_blocks = soup.find_all("li", attrs={"class":"block1 clearfix"})

    for block in data_blocks:
        rows = block.find_all("a")
        for row in rows:
            writer.writerow(row) # csv 작성


    
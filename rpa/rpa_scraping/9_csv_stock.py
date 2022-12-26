import csv
import requests
from bs4 import BeautifulSoup

# 시가총액 csv
# csv 파일 만들때는 참고로 리스트 형식으로 넣어야 함.


url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="
filename = "시가총액1-500.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") 
# newline을 통해 불필요한 줄바꿈 없애줌. utf-8-sig 를 통해 엑셀 한글 호환
writer = csv.writer(f)
title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split('\t')
# split('\t') 빈공간으로 항목 구별 res->[N, 종목명, ...]
writer.writerow(title)

for page in range(0,10):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find_all("tr", attrs={"onmouseover":"mouseOver(this)"})
    # 모든 줄 가져옴

    for row in data_rows:
        columns = row.find_all("td") # 각 줄
        if len(columns) <=1: # 의미없는 데이터 스킵
            continue 
        data = [column.get_text().strip() for column in columns] 
        # 각 줄의 각 요소, strip - 불필요한거 제외시켜줌
        # 한 줄 for 문
        writer.writerow(data) # csv 작성


    
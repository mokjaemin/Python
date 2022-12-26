import requests

# res = requests.get("http://nadocoing.tistory.com")
res = requests.get("http://google.com")
res.raise_for_status() # 1 문제가 있으면 아래 문장 아예 실행 안함



# 2
# print("응답코드 : ", res.status_code) # 200 이면 페이지에 접근 가능



# 3
# if res.status_code == requests.codes.ok:
#     print("정상적으로 페이지에 접근 가능")
# else:
#     print("문제가 생겼습니다. [에러코드] : ", res.status_code)


print(len(res.text)) # html 문서의 글자 개수

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text) # 해당 html의 text를 mygoogle.html 파일로 만들어 줌 
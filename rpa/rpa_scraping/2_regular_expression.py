import re

# 정규식 정리
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. p.search("비교할 문자열") : 주어진 문자열에서 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든것을 리스트 형태로 반환

# 원하는 형태
# . : 은 '하나'의 문자 의미
# ^ : 문자열의 시작을 의미 ex) (^de) -> de로 시작
# $ : 문자열의 끝을 의미 ex) (se$) -> se로 끝남




# ca?e 에서 물음표 찾기

p = re.compile("ca.e")
# . : 은 '하나'의 문자 의미
# ^ : 문자열의 시작을 의미 ex) (^de) -> de로 시작
# $ : 문자열의 끝을 의미 ex) (se$) -> se로 끝남


def print_match(a):
    if a:
        print("group() : ", a.group()) # 일치하는 문자열을 반환
        print("string : ", a.string) # 입력받은 문자열 반환
        print("start : ", a.start()) # 일치하는 문자열의 시작 인덱스
        print("end : ", a.end()) # 일치하는 문자열의 끝 인덱스
        print("span : ", a.span()) # 일치하는 문자열의 시작과 끝 인덱스 함께 출력
    else:
        print("매칭 되지 않음")


# m = p.match("careless") # 주어진 문자열이 처음부터 일치하는 지 확인.
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는 것이 있는지 확인.
# print_match(m)

lst = p.findall("care, cafe") # 일치하는 모든 것을 리스트 형태로 반환.
print(lst)
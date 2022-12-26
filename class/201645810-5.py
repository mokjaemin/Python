# 5

import re

from sympy import LessThan

def check(pwd):
    if len(pwd) < 10 :
        print("비밀번호는 최소 10자 이상이여야합니다.")
        return False
    elif len(pwd) >= 14 :
        print("비밀번호는 14자를 넘을 수 없습니다.")
        return False
    elif re.search('[0-9]+', pwd) is None :
        print("비밀번호는 최소 1개이상의 숫자를 포함해야 합니다.")
        return False
    elif re.search('[a-zA-Z]+', pwd) is None :
        print("비밀번호는 최소 1개이상의 영문자를 포함해야 합니다.")
        return False
    elif re.search('[`~!@#$%^&*(),<.>/?]+', pwd) is None:
        print('비밀번호는 최소 2개 이상의 특수문자가 포함되어야 함')  
        return False
    elif not pwd[0].isupper():
        print("비밀번호는 영문 대문자로 시작해야합니다.")
        return False
    elif re.search('[`~!@#$%^&*(),<.>/?]+', pwd) is not None:
        if len(re.search('[`~!@#$%^&*(),<.>/?]+', pwd).group()) < 2:
            print('비밀번호는 최소 2개 이상의 특수문자가 포함되어야 함')  
            return False
        else :
            print("올바른 비밀번호입니다.")
    else:
        print("올바른 비밀번호입니다.")

pwd = 1
while(pwd != 0) :
    pwd = input("비밀번호를 입력하시오")
    check(pwd)
    
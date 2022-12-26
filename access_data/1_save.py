import json
import pickle

x = ['a', 'b', 'c']
f = open("binary.txt", "w", encoding="utf-8")
json.dump(x, f)
f.close()

# json 과 pickle 차이
# pickle은 더 큰 용량의 파일을 저장하기에 용이
# "wb" - 바이너리 형태로 저장하기에 용량 차지 적음
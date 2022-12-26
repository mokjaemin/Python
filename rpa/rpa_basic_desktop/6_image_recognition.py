from PIL.ImageOps import grayscale
import pyautogui
import time 
import sys

import cv2
import numpy as np
import pyautogui

# 맥북은 조정이 필요함 새로운 함수 찾을 수 있도록 !!!!!!!!!!!










# 이거 잘 안됨....
# file_trash = pyautogui.locateOnScreen("trash.png")
# print(file_trash)
# pyautogui.moveTo(file_trash)
# # pyautogui.moveTo(file_trash)
# 해당 그림에 해당하는 곳의 위치를 반환후 클릭
# pyautogui.click(file_trash)



# 해당사진이 여러개 있을 경우 (all 과 all x 차이)
# for i in pyautogui.locateAllOnScreen("trash.png"):
#     print(i)





# 속도 개선
# 1. GrayScale
# file_trash = pyautogui.locateOnScreen("trash.png", grayscale=True)
# pyautogui.moveTo(file_trash)





# 2. 범위 지정
# file_trash = pyautogui.locateOnScreen("trash.png", region=(1213, 528, 1421-1213, 579-528))
# pyautogui.moveTo(file_trash)
#1213,528 1421,579





# 3. 정확도 조정
# file_start = pyautogui.locateOnScreen("start.png", confidence = 0.7)
# pyautogui.moveTo(file_start)
# pip3 install opencv-python 설치후 confidence 조절을 통해 정확도 조절 낮을수록 정확도 낮아지면서 빨라짐





# 자동화 대상이 바로 보이지 않는 경우1 - 없으면 끝냄
# file_start = pyautogui.locateOnScreen("start.png")
# if file_start:
#     pyautogui.click(file_start)
# else:
#     print("발견 못함")





# # 자동화 대상이 바로 보이지 않는 경우2 - 찾으면 동작 실행
# while file_start is None:
#     file_start = pyautogui.locateOnScreen("start.png")
#     print("발견실패") # 발견하면 while 문 벗어나면서 밑에 문장 실행

# pyautogui.click(file_start)





# # 일정시간동안 기다리기

# timeout = 10 # 10초 대기
# start = time.time() # 시작 시간 설정
# file_start = None
# while file_start is  None:
#     file_start = pyautogui.locateOnScreen("memo.png")
#     end = time.time() # 종료시간 설정
#     if end - start > timeout: # 지정한 10초 초과하면
#         print("시간 종료")
#         sys.exit()
# pyautogui.click((file_start[0]/2 + 20, file_start[1]/2 + 12))






# 위의 내용 함수화
def find_target(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target


def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target[0]/2 + 20, target[1]/2 + 12)
    else:
        print(f"[timeout {timeout}s] target not found ({img_file}). Terminate program")
        sys.exit()

# # 사용

my_click("safari.png", 5)
# pyautogui.click(1427, 76)
my_click("pnu.png", 5)
# pyautogui.mouseInfo()




# locate = pyautogui.locateOnScreen("memo.png")
# print(locate)
# pyautogui.moveTo(locate[0]/2 + 20, locate[1]/2 + 12)
# # pyautogui.mouseInfo()
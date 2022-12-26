import pyautogui

# pyautogui.mouseInfo() # 마우스 위치에 따른 좌표정보와 색깔 정보를 가져옴
pyautogui.PAUSE = 1 # 동작 하나하나에 sleep 적용

# for 문을 사용한 마우스 연속 움직임, 마우스를 화면 구석에 옮길시 동작 종료
for i in range(5):
    pyautogui.move(100,100)

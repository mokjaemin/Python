import pyautogui

# pyautogui.sleep(3) # 3초기다림
# print(pyautogui.position())

# pyautogui.click(108, 8, duration=1) # 해당 위치 클릭, 해당시간 동안 이동 후
# click = mouseDown() + mouseUp()
# doubleClick() = click(clicks=2) 더블 클릭, 횟수 설정시 횟수 만큼 클릭


# 스크랩
# pyautogui.moveTo(100,100)
# pyautogui.mouseDown()
# pyautogui.moveTo(200,200)
# pyautogui.mouseUp()

#  우크릭, 휠클릭
# pyautogui.rightClick()
# pyautogui.middleClick()

# 드래그
# pyautogui.drag(100,100) # 현재 마우스 위치로 부터 100, 100 만큼 대상을 이동시킴 
# pyautogui.dragTo(100,100) # 해당 위치로 대상을 이동 시킴

#스크롤
pyautogui.scroll(300) # 양수면 위로, 음수면 아래로 스크롤
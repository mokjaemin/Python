import pyautogui

# 절대 좌표로 마우스 이동
#pyautogui.moveTo(100,100) # 지정한 위치로 마우스 이동 (가로, 세로)
# pyautogui.moveTo(100, 200, duration=5) #5초동안 해당 위치로 이동, 클수록 오래걸림

# pyautogui.moveTo(100, 200, duration=3)
# pyautogui.moveTo(200, 200, duration=3)
# pyautogui.moveTo(300, 200, duration=3)

# 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로 부터)
# pyautogui.moveTo(100, 200)
# pyautogui.move(100, 200) #위에서 실행된 100,100을 기준으로 +100, +200 실행
# pyautogui.move(100, 200) #result  300, 600

# # 결과 보기
# print(pyautogui.position())

# 해당 마우스의 위치 찾기
p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)
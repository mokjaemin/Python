from os import terminal_size
from posix import times_result
import pyautogui
import pyperclip

# pyautogui.write("12345", interval=1) # interval = 1 means 1 sec to write it
# pyautogui.write(["t", "e", "s", "t", "left", "left" ,"right", "s", "enter"], interval=1)
# 방향키 left right,  엔터 enter

# 특수문자 $ (shift + 4)
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 command + a
# pyautogui.keyDown("command")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("command")

# 간편한 조합키 (ma에서 안되는데 이유를 모르겠음. command 만 안됨)
# pyautogui.hotkey("command", "a")
# 순서대로 누르고 땜

# 한글 입력 (import pyperclip 필요)
# pyperclip.copy("재민")
# pyautogui.keyDown("command")
# pyautogui.keyDown("v")
# pyautogui.keyUp("v")
# pyautogui.keyUp("command")

# + 함수 정의
# def k_write(text):
#     pyperclip.copy(text)
#     pyautogui.keyDown("command")
#     pyautogui.keyDown("v")
#     pyautogui.keyUp("v")
#     pyautogui.keyUp("command")

# k_write("재민")


# 자동화 프로그램 종료
# command + shift + option + q
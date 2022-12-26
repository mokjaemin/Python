import pyautogui
from pyscreeze import pixel
#  스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 82,13 NA_on_macOS NA_on_macOS

# 내가 클릭하려는 위치의 픽셀이 해당 픽셀과 동일한지 용이
pixel = pyautogui.pixel(82, 13)
print(pixel) # 해당위치의 RGB 값 출력
print(pyautogui.pixelMatchesColor(82, 13, pixel)) # 해당 위치의 픽셀과 색깔 비교
print(pyautogui.pixelMatchesColor(82, 13, (43, 46, 72))) # 위와 동일한 기능
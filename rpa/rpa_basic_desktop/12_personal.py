from PIL.ImageOps import grayscale
import pyautogui
import time 
import sys

import cv2
import numpy as np
import pyautogui




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
        pyautogui.click(target[0]/2 + 22, target[1]/2 + 15)
    else:
        print(f"[timeout {timeout}s] target not found ({img_file}). Terminate program")
        sys.exit()


# pyautogui.mouseInfo()

# pyautogui.click(219, 864, duration=1)
# pyautogui.click(1427, 76, duration=1)
# pyautogui.click(522, 220, duration=1)
# pyautogui.click(934, 286, duration=1)
# pyautogui.write("201645810")
# pyautogui.click(1106, 290, duration=1)
# pyautogui.write("ahrwoals11!!")
# pyautogui.click(1234, 290)
# my_click("pngfile/webmail.png", 10)

pyautogui.click(219, 864)
pyautogui.click(1427, 76, duration=0.7)
my_click("pngfile/pnu.png", 10)
pyautogui.click(934, 286, duration=1)
pyautogui.write("201645810")
pyautogui.click(1106, 290)
pyautogui.write("ahrwoals11!!")
my_click("pngfile/login.png", 10)
my_click("pngfile/webmail.png", 10)





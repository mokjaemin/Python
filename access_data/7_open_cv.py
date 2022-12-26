from matplotlib import cm
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


# 이미지 처리 및 사물 분류를 위한 도구


# import image
im = cv.imread('./access_data/pic1.jpg')

# BGR plot
# 원본사진과 다른 결과 출력 - BGR을 RGB로 바꿔줘야 함.
# plt.figure()
# plt.imshow(im)
# plt.title('original')
# plt.show()

# RGB 로 변경
rgb = cv.cvtColor(im, cv.COLOR_BGR2RGB)
# plt.figure()
# plt.imshow(rgb)
# plt.title('RGB')
# plt.show()

# Gray 로 변경
gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
# plt.figure()
# plt.imshow(gray, cmap='gray') # 위와 달리 cmap = gray 작성해야함
# plt.title('GRAY') 
# plt.show()

# blur
blur = cv.blur(im, (50,50))
blur = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

# 가로 한줄 세로 두줄의 첫번쨰 사진
# plt.subplot(121)
# plt.imshow(rgb)
# plt.title('RGB')
# # 가로 한줄 세로 두줄의 두번쨰 사진
# plt.subplot(122)
# plt.imshow(blur)
# plt.title('BLUR')
# plt.show()

# edge detection
edges = cv.Canny(gray, 0, 100) # 숫자가 작을수록 edge detect 강도가 쎄짐
plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.title('GRAY')
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('EDGE DETECTION')
plt.show()
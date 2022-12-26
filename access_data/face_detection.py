import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# 이미지 로드
img1 = cv.imread('./access_data/pic1.jpg')

# rgb로 변경
rgb = cv.cvtColor(img1, cv.COLOR_BGR2RGB)

# gray로 변경
gray = cv.cvtColor(rgb, cv.COLOR_RGB2GRAY)

# classifier 설정
classifier = cv.CascadeClassifier('./access_data/haarcascade_frontalface_default.xml')


# 사각형 만들기
rects = classifier.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5
)

print("face Found : {}".format(len(rects)))

# rectangle trait
for x,y,w,h in rects:
    # 이미지에 사각형 그리기
    cv.rectangle(rgb, (x,y), (x+w,y+h), (0,255,0), 2) # 색깔, 선사이즈



# image plt
plt.imshow(rgb)
plt.show()

# save_pic
# bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
# cv.imwrite('find_faces.png', bgr)
from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("img.jpeg") # 이미지 로드, 해당 파일에 이미지 있어야 함.
ws.add_image(img, "C3") # 이미지 삽입

wb.save("james_image.xlsx")
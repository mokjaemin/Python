from openpyxl import Workbook
wb = Workbook() #새 워크북 생성 
ws = wb.active #현재 활성화된 시트를 가져옴
ws.title = "james1" #시트의 이름을 변경
wb.save("james.xlsx")
wb.close()
from openpyxl import load_workbook
wb = load_workbook("james.xlsx")
ws = wb.active

ws.insert_rows(8, 5)
# 8위치로 부터 5개의 줄 삽입
# rows -> cols 로 변경시 col 생성

wb.save("james_insert_row.xlsx")
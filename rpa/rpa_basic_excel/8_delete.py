from openpyxl import load_workbook
wb = load_workbook("james.xlsx")
ws = wb.active

ws.delete_rows(8, 3)
# 8번째 줄부터 총 3줄 삭제

wb.save("james_delete_rows.xlsx")
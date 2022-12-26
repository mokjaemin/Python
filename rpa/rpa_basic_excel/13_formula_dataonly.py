from openpyxl import load_workbook
wb = load_workbook("formula.xlsx", data_only=True)
#데이터 온리 때문에 수식이 아닌 실제 데이터 값을 엑셀에서 불러옴
ws = wb.active


# 위의 데이터온리가 없었다면 수식 그대로 가져옴
for row in ws.values:
    for cell in row:
        print(cell)

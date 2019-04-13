import xlrd

loc = ('Test.xlsx')

wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

try:
    for i in range(0, 100):
        print(sheet.cell_value(1, i))
except IndexError:
    print('Index Out Of Bounds')



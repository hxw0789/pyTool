import xlrd
# 读excel第一个sheet的的所有内容
workbook = xlrd.open_workbook(r'C:\Users\DELL\Desktop\20210629A1系统开发计划(1).xls')
table = workbook.sheets()[0]
effectRow = table.nrows
for row in range(effectRow):
    print(table.row_values(row))

import xlrd
data = xlrd.open_workbook('test.xls')
table = data.sheets()[0]
name = table.name
nrows = table.nrows
nclos = table.ncols
# row_value = table.row_values(1)
# col_value = table.col_values(5)
import openpyxl
wb = openpyxl.load_workbook('sample.xlsx')
sheet = wb.active
sheet.unmerge_cells('A2:D3')
wb.save('sample.xlsx')

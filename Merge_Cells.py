import openpyxl 
wb = openpyxl.Workbook() 
sheet = wb.active 
sheet.merge_cells('A2:D3') 
wb.save('sample.xlsx')
